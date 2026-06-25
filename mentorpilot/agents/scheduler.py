"""Agent 2 : Scheduler — déclenche la leçon quotidienne à une heure fixe."""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Awaitable, Callable, Optional

logger = logging.getLogger(__name__)


class Scheduler:
    """Boucle asyncio qui appelle un callback chaque jour à `hour` (heure locale)."""

    def __init__(self, hour: int):
        self.hour = max(0, min(23, hour))
        self.on_tick: Optional[Callable[[], Awaitable[None]]] = None
        self._task: Optional[asyncio.Task] = None
        self._stopped = asyncio.Event()

    def _seconds_until_next(self) -> float:
        now = datetime.now()
        target = now.replace(hour=self.hour, minute=0, second=0, microsecond=0)
        if target <= now:
            target += timedelta(days=1)
        return (target - now).total_seconds()

    async def _run(self) -> None:
        logger.info(f"Scheduler démarré — leçon quotidienne à {self.hour:02d}h00 (heure locale).")
        while not self._stopped.is_set():
            delay = self._seconds_until_next()
            logger.info(f"Prochaine leçon dans {delay / 3600:.1f}h.")
            try:
                await asyncio.wait_for(self._stopped.wait(), timeout=delay)
                return  # stop demandé
            except asyncio.TimeoutError:
                pass  # c'est l'heure
            if self.on_tick:
                try:
                    await self.on_tick()
                except Exception as e:
                    logger.error(f"Erreur pendant le tick quotidien : {e}")

    async def start(self) -> None:
        self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        self._stopped.set()
        if self._task:
            await self._task
