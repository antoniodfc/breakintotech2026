"""Persistance de l'état — un simple fichier JSON (un seul apprenant).

Pour gérer plusieurs apprenants plus tard, remplace ces deux fonctions
par un backend Redis/SQLite indexé par chat_id.
"""

import json
import logging
import os
import tempfile

from models import AppState

logger = logging.getLogger(__name__)


def load_state(path: str) -> AppState:
    """Charge l'état depuis le fichier JSON, ou retourne un état vide."""
    if not os.path.exists(path):
        logger.info("Aucun état existant — démarrage à vide.")
        return AppState()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return AppState.from_dict(json.load(f))
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        logger.error(f"État illisible ({e}) — repart à vide. Ancien fichier: {path}")
        return AppState()


def save_state(state: AppState, path: str) -> None:
    """Écrit l'état de façon atomique (write-then-rename)."""
    data = json.dumps(state.to_dict(), ensure_ascii=False, indent=2)
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
