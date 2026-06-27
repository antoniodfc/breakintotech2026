"""Agent 4 : Telegram Bot — interface de l'apprenant (onboarding, leçons, questions)."""

import logging
from enum import Enum
from typing import Awaitable, Callable, Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import Config
from models import AppState, LearningPlan, esc

logger = logging.getLogger(__name__)

_MAX_LEN = 3800  # marge sous la limite Telegram (4096)

LEVELS = [
    ("debutant_total", "🌱 Grand débutant"),
    ("quelques_bases", "🌿 Quelques bases"),
    ("intermediaire", "🌳 Intermédiaire"),
]


class Convo(str, Enum):
    """État de la conversation d'onboarding / d'interaction."""
    IDLE = "idle"
    AWAIT_GOAL = "await_goal"
    AWAIT_LEVEL = "await_level"
    AWAIT_ADJUST = "await_adjust"
    AWAIT_QUESTION = "await_question"


class TelegramBot:
    """Bot Telegram : pilote l'apprentissage depuis le téléphone.

    Callbacks branchés par l'orchestrateur :
      - on_create_plan(goal, level, adjust) -> LearningPlan
      - on_plan_accepted(plan) -> None
      - on_lesson_request() -> str
      - on_question(question) -> str
      - on_step_done() -> dict   {finished, next_title, streak, pct}
      - get_state() -> AppState
    """

    def __init__(self):
        self.app: Optional[Application] = None
        self._convo: Convo = Convo.IDLE
        self._draft_goal: str = ""
        self._draft_level: str = ""
        self._pending_plan: Optional[LearningPlan] = None

        self.on_create_plan: Optional[Callable[[str, str, Optional[str]], Awaitable[LearningPlan]]] = None
        self.on_plan_accepted: Optional[Callable[[LearningPlan], Awaitable[None]]] = None
        self.on_lesson_request: Optional[Callable[[], Awaitable[str]]] = None
        self.on_question: Optional[Callable[[str], Awaitable[str]]] = None
        self.on_step_done: Optional[Callable[[], Awaitable[dict]]] = None
        self.get_state: Optional[Callable[[], AppState]] = None

    # ---- Cycle de vie ----

    async def start(self) -> None:
        self.app = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()

        self.app.add_handler(CommandHandler("start", self._cmd_start))
        self.app.add_handler(CommandHandler("plan", self._cmd_plan))
        self.app.add_handler(CommandHandler("lesson", self._cmd_lesson))
        self.app.add_handler(CommandHandler("status", self._cmd_status))
        self.app.add_handler(CommandHandler("next", self._cmd_next))
        self.app.add_handler(CommandHandler("restart", self._cmd_restart))
        self.app.add_handler(CommandHandler("cancel", self._cmd_cancel))
        self.app.add_handler(CallbackQueryHandler(self._handle_callback))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_text))

        await self.app.initialize()
        await self.app.start()
        await self.app.updater.start_polling()
        logger.info("Telegram bot started")

        await self._send(
            "🤖 *MentorPilot est en ligne !*\n\n"
            "Je suis ton mentor tech personnel.\n"
            "Tape /start pour définir ton objectif et générer ta roadmap."
        )

    async def stop(self) -> None:
        if self.app:
            await self.app.updater.stop()
            await self.app.stop()
            await self.app.shutdown()

    # ---- Push (appelé par le scheduler via l'orchestrateur) ----

    async def push_lesson(self) -> None:
        """Génère et envoie la leçon de l'étape en cours, avec boutons d'action."""
        if not self.on_lesson_request:
            return
        text = await self.on_lesson_request()
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("✅ Terminé", callback_data="lesson:done"),
            InlineKeyboardButton("❓ Une question", callback_data="lesson:question"),
        ]])
        await self._send(f"📚 *Leçon du jour*\n\n{text}", reply_markup=keyboard, parse_mode=None)

    # ---- Commandes ----

    async def _cmd_start(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        state = self.get_state() if self.get_state else AppState()
        if state.has_plan:
            await update.message.reply_text(
                "👋 Content de te revoir !\n\n"
                f"Tu travailles déjà sur : *{esc(state.plan.goal)}*.\n"
                "Commandes : /lesson · /plan · /status · /restart",
                parse_mode="Markdown",
            )
            return
        self._convo = Convo.AWAIT_GOAL
        await update.message.reply_text(
            "👋 *Bienvenue !*\n\n"
            "Je vais te construire un parcours d'apprentissage sur mesure.\n\n"
            "🎯 *Quel est ton objectif ?*\n"
            "_Ex : « devenir développeur web front-end », « apprendre Python pour la data »_",
            parse_mode="Markdown",
        )

    async def _cmd_plan(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        state = self.get_state() if self.get_state else AppState()
        if not state.has_plan:
            await update.message.reply_text("Aucune roadmap encore. Tape /start pour commencer.")
            return
        await update.message.reply_text(state.plan.telegram_preview, parse_mode="Markdown")

    async def _cmd_lesson(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        state = self.get_state() if self.get_state else AppState()
        if not state.has_plan:
            await update.message.reply_text("Définis d'abord ta roadmap avec /start.")
            return
        if state.is_finished:
            await update.message.reply_text("🎉 Tu as terminé toute ta roadmap ! Tape /restart pour un nouvel objectif.")
            return
        await update.message.reply_text("⏳ Je prépare ta leçon...")
        await self.push_lesson()

    async def _cmd_status(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        state = self.get_state() if self.get_state else AppState()
        if not state.has_plan:
            await update.message.reply_text("Pas encore de parcours. Tape /start.")
            return
        m = state.current_milestone()
        current = f"{esc(m.title)} ({m.index + 1}/{len(state.plan.milestones)})" if m else "Terminé 🎉"
        await update.message.reply_text(
            f"📊 *Ta progression*\n\n"
            f"🎯 Objectif : {esc(state.plan.goal)}\n"
            f"📍 Étape en cours : {current}\n"
            f"✅ Étapes terminées : {len(state.progress.completed)}/{len(state.plan.milestones)} "
            f"({state.progress_pct()}%)\n"
            f"🔥 Série : {state.progress.streak} jour(s)",
            parse_mode="Markdown",
        )

    async def _cmd_next(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Marque l'étape en cours comme terminée (équivalent du bouton ✅)."""
        if not self._is_authorized(update):
            return
        await self._complete_step(notify=update.message.reply_text)

    async def _cmd_restart(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        self._convo = Convo.AWAIT_GOAL
        self._pending_plan = None
        await update.message.reply_text(
            "🔄 *Nouveau départ.*\n\n🎯 Quel est ton nouvel objectif ?",
            parse_mode="Markdown",
        )

    async def _cmd_cancel(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        self._convo = Convo.IDLE
        await update.message.reply_text("🚫 Annulé.")

    # ---- Boutons ----

    async def _handle_callback(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        if not query or not self._is_authorized_callback(query):
            return
        await query.answer()

        parts = query.data.split(":", 1)
        if len(parts) != 2:
            return
        action, value = parts

        if action == "level":
            await self._on_level_chosen(query, value)
        elif action == "plan" and value == "accept":
            await self._on_plan_accept(query)
        elif action == "plan" and value == "adjust":
            self._convo = Convo.AWAIT_ADJUST
            await query.edit_message_text(
                "✏️ Dis-moi ce que tu veux changer.\n"
                "_Ex : « plus court », « ajoute du SQL », « commence plus facile »_",
                parse_mode="Markdown",
            )
        elif action == "lesson" and value == "done":
            await self._complete_step(notify=lambda t, **k: self._send(t))
        elif action == "lesson" and value == "question":
            self._convo = Convo.AWAIT_QUESTION
            await self._send("❓ Pose-moi ta question, je t'écoute.")

    async def _on_level_chosen(self, query, level_key: str):
        label = dict(LEVELS).get(level_key, level_key)
        self._draft_level = label
        self._convo = Convo.IDLE
        await query.edit_message_text(f"✅ Niveau : {label}\n\n⏳ Je construis ta roadmap...")
        await self._generate_and_show_plan()

    async def _on_plan_accept(self, query):
        if not self._pending_plan:
            await query.edit_message_text("⚠️ Plan expiré. Tape /start.")
            return
        if self.on_plan_accepted:
            await self.on_plan_accepted(self._pending_plan)
        self._pending_plan = None
        self._convo = Convo.IDLE
        await query.edit_message_text(
            "🚀 *C'est parti !*\n\n"
            "Tu recevras une leçon chaque jour. Tu peux aussi taper /lesson quand tu veux.",
            parse_mode="Markdown",
        )
        await self.push_lesson()

    # ---- Texte libre ----

    async def _handle_text(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not self._is_authorized(update):
            return
        text = update.message.text.strip()

        if self._convo == Convo.AWAIT_GOAL:
            self._draft_goal = text
            self._convo = Convo.AWAIT_LEVEL
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(label, callback_data=f"level:{key}")]
                for key, label in LEVELS
            ])
            await update.message.reply_text(
                f"🎯 Objectif : *{esc(text)}*\n\n📊 Quel est ton niveau actuel ?",
                parse_mode="Markdown", reply_markup=keyboard,
            )
            return

        if self._convo == Convo.AWAIT_ADJUST:
            self._convo = Convo.IDLE
            await update.message.reply_text("⏳ Je réajuste ta roadmap...")
            await self._generate_and_show_plan(adjust=text)
            return

        if self._convo == Convo.AWAIT_QUESTION:
            self._convo = Convo.IDLE
            if self.on_question:
                await update.message.reply_text("⏳ Je réfléchis...")
                answer = await self.on_question(text)
                await self._send(answer, parse_mode=None)
            return

        # IDLE : si une roadmap existe, on traite le texte comme une question.
        state = self.get_state() if self.get_state else AppState()
        if state.has_plan and self.on_question:
            await update.message.reply_text("⏳ Je réfléchis...")
            answer = await self.on_question(text)
            await self._send(answer, parse_mode=None)
        else:
            await update.message.reply_text("💡 Tape /start pour définir ton objectif.")

    # ---- Logique partagée ----

    async def _generate_and_show_plan(self, adjust: Optional[str] = None):
        if not self.on_create_plan:
            return
        plan = await self.on_create_plan(self._draft_goal, self._draft_level, adjust)
        self._pending_plan = plan
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton("✅ Valider", callback_data="plan:accept"),
            InlineKeyboardButton("✏️ Ajuster", callback_data="plan:adjust"),
        ]])
        await self._send(
            f"{plan.telegram_preview}\n\n_Ça te convient ?_",
            reply_markup=keyboard,
        )

    async def _complete_step(self, notify):
        if not self.on_step_done:
            return
        state = self.get_state() if self.get_state else AppState()
        if not state.has_plan or state.is_finished:
            await notify("Rien à valider. Tape /start ou /restart.")
            return
        result = await self.on_step_done()
        if result.get("finished"):
            await notify(
                f"🎉 *Bravo, tu as terminé toute ta roadmap !*\n"
                f"🔥 Série : {result.get('streak', 0)} jour(s)\n\n"
                f"Tape /restart pour viser un nouvel objectif.",
                parse_mode="Markdown",
            )
        else:
            await notify(
                f"✅ Étape validée ! ({result.get('pct', 0)}%)\n"
                f"🔥 Série : {result.get('streak', 0)} jour(s)\n"
                f"➡️ Prochaine étape : *{esc(result.get('next_title', ''))}*\n\n"
                f"Tape /lesson pour enchaîner.",
                parse_mode="Markdown",
            )

    # ---- Helpers ----

    def _is_authorized(self, update: Update) -> bool:
        return bool(update.effective_chat and update.effective_chat.id == Config.TELEGRAM_CHAT_ID)

    def _is_authorized_callback(self, query) -> bool:
        return bool(query.message and query.message.chat_id == Config.TELEGRAM_CHAT_ID)

    async def _send(self, text: str, reply_markup=None, parse_mode: Optional[str] = "Markdown"):
        if not self.app:
            return None
        if len(text) > _MAX_LEN:
            text = text[:_MAX_LEN] + "…"
        try:
            return await self.app.bot.send_message(
                chat_id=Config.TELEGRAM_CHAT_ID,
                text=text,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
            )
        except Exception as e:
            logger.error(f"Telegram send error: {e}")
            # Réessai en texte brut si le Markdown a planté
            if parse_mode is not None:
                try:
                    return await self.app.bot.send_message(
                        chat_id=Config.TELEGRAM_CHAT_ID, text=text, reply_markup=reply_markup,
                    )
                except Exception:
                    pass
            return None
