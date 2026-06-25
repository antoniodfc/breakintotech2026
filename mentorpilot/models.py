"""Modèles de données partagés par la flotte d'agents."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional


def esc(s: str) -> str:
    """Échappe les caractères spéciaux du Markdown v1 de Telegram."""
    for ch in ("_", "*", "`", "["):
        s = s.replace(ch, f"\\{ch}")
    return s


@dataclass
class Milestone:
    """Une étape de la roadmap d'apprentissage."""
    index: int
    title: str
    concept: str          # de quoi parle l'étape (pour guider le Tutor)
    est_days: int = 3
    done: bool = False


@dataclass
class LearningPlan:
    """Roadmap personnalisée générée par le Planner et validée par l'apprenant."""
    goal: str
    level: str
    milestones: list[Milestone] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "LearningPlan":
        milestones = [Milestone(**m) for m in d.get("milestones", [])]
        return cls(
            goal=d["goal"],
            level=d["level"],
            milestones=milestones,
            created_at=d.get("created_at", datetime.utcnow().isoformat()),
        )

    @property
    def telegram_preview(self) -> str:
        """Aperçu Markdown de la roadmap pour validation."""
        lines = [
            f"🎯 *Objectif :* {esc(self.goal)}",
            f"📊 *Niveau :* {esc(self.level)}",
            "━━━━━━━━━━━━━━━",
            "*Ta roadmap :*",
        ]
        for m in self.milestones:
            check = "✅" if m.done else f"{m.index + 1}."
            lines.append(f"{check} {esc(m.title)}  _({m.est_days}j)_")
        return "\n".join(lines)


@dataclass
class Progress:
    """Suivi de l'avancement de l'apprenant."""
    current_step: int = 0
    day_index: int = 0
    completed: list[int] = field(default_factory=list)
    last_active: str = ""
    streak: int = 0
    last_lesson_date: str = ""   # YYYY-MM-DD — évite les doublons du scheduler


@dataclass
class AppState:
    """État global persisté (un seul apprenant)."""
    plan: Optional[LearningPlan] = None
    progress: Progress = field(default_factory=Progress)

    def to_dict(self) -> dict:
        return {
            "plan": self.plan.to_dict() if self.plan else None,
            "progress": asdict(self.progress),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "AppState":
        plan = LearningPlan.from_dict(d["plan"]) if d.get("plan") else None
        progress = Progress(**d["progress"]) if d.get("progress") else Progress()
        return cls(plan=plan, progress=progress)

    # ---- Helpers ----

    @property
    def has_plan(self) -> bool:
        return self.plan is not None and len(self.plan.milestones) > 0

    @property
    def is_finished(self) -> bool:
        return self.has_plan and self.progress.current_step >= len(self.plan.milestones)

    def current_milestone(self) -> Optional[Milestone]:
        if not self.has_plan or self.is_finished:
            return None
        return self.plan.milestones[self.progress.current_step]

    def progress_pct(self) -> int:
        if not self.has_plan:
            return 0
        return round(100 * len(self.progress.completed) / len(self.plan.milestones))
