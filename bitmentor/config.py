"""Configuration — chargée depuis le fichier .env."""

import os
import sys
from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    """Retourne la valeur d'une variable d'env obligatoire, quitte si absente."""
    val = os.getenv(key, "").strip()
    if not val:
        print(f"[ERREUR] Variable d'environnement manquante : {key}", file=sys.stderr)
        print("         Copie .env.example vers .env et remplis les valeurs.", file=sys.stderr)
        sys.exit(1)
    return val


class Config:
    # DeepSeek (API compatible OpenAI)
    DEEPSEEK_API_KEY = _require("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")

    # Telegram
    TELEGRAM_BOT_TOKEN = _require("TELEGRAM_BOT_TOKEN")

    @staticmethod
    def get_telegram_chat_id() -> int:
        raw = os.getenv("TELEGRAM_CHAT_ID", "").strip()
        if not raw or not raw.lstrip("-").isdigit():
            print("[ERREUR] TELEGRAM_CHAT_ID manquant ou invalide.", file=sys.stderr)
            print("         Obtiens ton chat ID via @userinfobot sur Telegram.", file=sys.stderr)
            sys.exit(1)
        return int(raw)

    TELEGRAM_CHAT_ID: int = 0  # résolu juste après la définition de la classe

    # Persistance (1 apprenant → un simple fichier JSON)
    STATE_PATH = os.getenv("STATE_PATH", "./state.json")

    # Scheduler — heure (locale) du push de la leçon quotidienne, 0–23
    LESSON_HOUR = int(os.getenv("LESSON_HOUR", "9"))


# Résolution différée du TELEGRAM_CHAT_ID pour que _require soit appelé au runtime
Config.TELEGRAM_CHAT_ID = Config.get_telegram_chat_id()
