FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# L'état est écrit dans /app/data/state.json (STATE_PATH) — dossier monté
# en volume via docker-compose pour persister entre redémarrages.
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "orchestrator.py"]
