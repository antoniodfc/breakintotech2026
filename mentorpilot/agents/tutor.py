"""Agent 3 : Tutor — génère la leçon du jour et répond aux questions de l'apprenant."""

import logging

from openai import OpenAI

from config import Config
from models import LearningPlan, Milestone

logger = logging.getLogger(__name__)

_TONE = (
    "Tu es un mentor tech bienveillant qui s'adresse à un GRAND DÉBUTANT. "
    "Tu expliques simplement, avec des analogies du quotidien, sans jargon non expliqué. "
    "Tu es encourageant et concret. Tu écris en français."
)

LESSON_PROMPT = (
    _TONE
    + "\n\nProduis la LEÇON DU JOUR pour l'étape en cours. Structure attendue :\n"
    "1. Un titre court.\n"
    "2. L'explication du concept en 5-10 lignes max, avec un exemple concret.\n"
    "3. UN seul petit exercice pratique faisable en 15-20 min.\n"
    "Reste bref : c'est une dose quotidienne, pas un cours complet. "
    "N'utilise pas de mise en forme Markdown complexe (pas de tableaux)."
)

QUESTION_PROMPT = (
    _TONE
    + "\n\nL'apprenant pose une question pendant son étape en cours. "
    "Réponds de façon claire et courte (quelques phrases). "
    "Si la question sort du sujet de l'étape, réponds quand même brièvement puis "
    "ramène-le gentiment vers son objectif."
)


class Tutor:
    """Génère le contenu pédagogique via DeepSeek."""

    def __init__(self):
        self.client = OpenAI(
            api_key=Config.DEEPSEEK_API_KEY,
            base_url=Config.DEEPSEEK_BASE_URL,
        )

    def generate_lesson(self, plan: LearningPlan, milestone: Milestone, day_index: int) -> str:
        context = (
            f"Objectif global : {plan.goal}\n"
            f"Niveau : {plan.level}\n"
            f"Étape en cours ({milestone.index + 1}/{len(plan.milestones)}) : {milestone.title}\n"
            f"Thème de l'étape : {milestone.concept}\n"
            f"Jour d'apprentissage n°{day_index + 1}."
        )
        return self._chat(LESSON_PROMPT, context, max_tokens=900,
                          fallback=(
                              f"📚 {milestone.title}\n\n{milestone.concept}\n\n"
                              "Exercice : cherche un exemple simple de ce thème et reproduis-le toi-même. "
                              "(L'IA est indisponible pour l'instant — réessaie plus tard avec /lesson.)"
                          ))

    def answer_question(self, plan: LearningPlan, milestone: Milestone | None, question: str) -> str:
        step = (
            f"Étape en cours : {milestone.title} — {milestone.concept}"
            if milestone else "Pas d'étape en cours."
        )
        context = (
            f"Objectif global : {plan.goal}\n"
            f"{step}\n\n"
            f"Question de l'apprenant : {question}"
        )
        return self._chat(QUESTION_PROMPT, context, max_tokens=600,
                          fallback="Désolé, je n'arrive pas à répondre là tout de suite. Réessaie dans un moment 🙏")

    # ---- Interne ----

    def _chat(self, system: str, user: str, max_tokens: int, fallback: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=Config.LLM_MODEL,
                max_tokens=max_tokens,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Erreur Tutor ({e})")
            return fallback
