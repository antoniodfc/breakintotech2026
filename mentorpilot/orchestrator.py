"""Orchestrateur — câble tous les agents dans une seule boucle d'événements.

Point d'entrée. Il :
1. Charge l'état (roadmap + progression) depuis state.json
2. Démarre le bot Telegram (interface apprenant)
3. Démarre le scheduler (push de la leçon quotidienne)
4. Branche les callbacks : Planner, Tutor, et les mutations d'état
"""

import asyncio
import logging
import signal
from datetime import datetime, timezone

from config import Config
from models import AppState, LearningPlan, Progress
from state import load_state, save_state
from agents.planner import Planner
from agents.tutor import Tutor
from agents.scheduler import Scheduler
from agents.telegram_bot import TelegramBot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("orchestrator")


def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


class Orchestrator:
    def __init__(self):
        self.state: AppState = load_state(Config.STATE_PATH)
        self.planner = Planner()
        self.tutor = Tutor()
        self.bot = TelegramBot()
        self.scheduler = Scheduler(Config.LESSON_HOUR)

    def _save(self) -> None:
        save_state(self.state, Config.STATE_PATH)

    # ---- Callbacks Planner ----

    async def create_plan(self, goal: str, level: str, adjust: str | None) -> LearningPlan:
        # Appel LLM synchrone → exécuté dans un thread pour ne pas bloquer la boucle
        return await asyncio.to_thread(self.planner.create_plan, goal, level, adjust)

    async def plan_accepted(self, plan: LearningPlan) -> None:
        self.state.plan = plan
        self.state.progress = Progress(last_active=datetime.now(timezone.utc).isoformat())
        self._save()
        logger.info(f"Roadmap acceptée : '{plan.goal}' ({len(plan.milestones)} étapes)")

    # ---- Callbacks Tutor ----

    async def lesson_request(self) -> str:
        m = self.state.current_milestone()
        if not m:
            return "🎉 Tu as terminé toute ta roadmap ! Tape /restart pour un nouvel objectif."
        lesson = await asyncio.to_thread(
            self.tutor.generate_lesson, self.state.plan, m, self.state.progress.day_index
        )
        self.state.progress.day_index += 1
        self.state.progress.last_lesson_date = _today()
        self.state.progress.last_active = datetime.now(timezone.utc).isoformat()
        self._save()
        return lesson

    async def question(self, q: str) -> str:
        m = self.state.current_milestone()
        return await asyncio.to_thread(self.tutor.answer_question, self.state.plan, m, q)

    # ---- Callback progression ----

    async def step_done(self) -> dict:
        m = self.state.current_milestone()
        if not m:
            return {"finished": True, "streak": self.state.progress.streak, "pct": 100}

        m.done = True
        if m.index not in self.state.progress.completed:
            self.state.progress.completed.append(m.index)
        self.state.progress.current_step += 1
        self.state.progress.streak += 1
        self.state.progress.last_active = datetime.now(timezone.utc).isoformat()
        self._save()

        if self.state.is_finished:
            return {"finished": True, "streak": self.state.progress.streak, "pct": 100}
        nxt = self.state.current_milestone()
        return {
            "finished": False,
            "next_title": nxt.title if nxt else "",
            "streak": self.state.progress.streak,
            "pct": self.state.progress_pct(),
        }

    # ---- Callback scheduler ----

    async def daily_tick(self) -> None:
        if not self.state.has_plan or self.state.is_finished:
            logger.info("Tick quotidien ignoré (pas de roadmap active).")
            return
        if self.state.progress.last_lesson_date == _today():
            logger.info("Leçon déjà envoyée aujourd'hui — tick ignoré.")
            return
        logger.info("Tick quotidien → envoi de la leçon.")
        await self.bot.push_lesson()

    # ---- Démarrage ----

    def _wire(self) -> None:
        self.bot.on_create_plan = self.create_plan
        self.bot.on_plan_accepted = self.plan_accepted
        self.bot.on_lesson_request = self.lesson_request
        self.bot.on_question = self.question
        self.bot.on_step_done = self.step_done
        self.bot.get_state = lambda: self.state
        self.scheduler.on_tick = self.daily_tick

    async def run(self) -> None:
        self._wire()
        await self.bot.start()
        await self.scheduler.start()
        logger.info("MentorPilot démarré. En attente d'événements...")

        stop = asyncio.Event()
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, stop.set)
            except NotImplementedError:
                pass  # non supporté sur certaines plateformes (ex : Windows)
        await stop.wait()

        logger.info("Arrêt en cours...")
        await self.scheduler.stop()
        await self.bot.stop()
        self._save()


if __name__ == "__main__":
    asyncio.run(Orchestrator().run())
