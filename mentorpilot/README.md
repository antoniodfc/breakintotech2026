# MentorPilot — Mentor IA pour débutants en tech

> Une flotte d'agents Python qui accompagne un débutant vers son objectif tech :
> **objectif → roadmap personnalisée → leçon quotidienne → questions → progression**

Tu donnes ton objectif (ex : *« devenir développeur web »*) et ton niveau → l'agent **Planner** génère une roadmap avec DeepSeek → tu la valides → chaque jour le **Scheduler** te pousse une leçon rédigée par le **Tutor** sur **Telegram**. Tu poses tes questions, tu valides tes étapes, et MentorPilot suit ta progression.

C'est le pendant « apprentissage » d'[InboxPilot](../inbox-pilot-ai-agents) : même architecture (flotte d'agents + human-in-the-loop + Telegram + Docker), un autre domaine.

---

## Comment ça marche

```
        /start (objectif + niveau)
              │
              ▼
     ┌─────────────────┐
     │  Planner         │  DeepSeek — génère la roadmap (6-10 étapes)
     └────────┬────────┘
              │  ✅ valider / ✏️ ajuster   (human-in-the-loop)
              ▼
     ┌─────────────────┐
     │  Scheduler       │  déclenche la leçon chaque jour à LESSON_HOUR
     └────────┬────────┘
              ▼
     ┌─────────────────┐     ┌──────────────────┐
     │  Tutor           │◄───►│  Ton téléphone    │
     │  DeepSeek        │     │  (Telegram)       │
     │  leçon + Q/R     │     └──────────────────┘
     └────────┬────────┘
              │  ✅ Terminé
              ▼
     ┌─────────────────┐
     │  Progression     │  state.json — étape suivante, série, %
     └─────────────────┘
```

---

## Les 4 agents (MVP)

| Agent | Fichier | Rôle |
|-------|---------|------|
| **Planner** | [`agents/planner.py`](agents/planner.py) | Objectif + niveau → roadmap (DeepSeek) |
| **Scheduler** | [`agents/scheduler.py`](agents/scheduler.py) | Pousse la leçon du jour à heure fixe |
| **Tutor** | [`agents/tutor.py`](agents/tutor.py) | Rédige la leçon + répond aux questions (DeepSeek) |
| **Telegram Bot** | [`agents/telegram_bot.py`](agents/telegram_bot.py) | Interface apprenant (onboarding, validation, Q/R) |

L'état (roadmap + progression) est persisté dans `state.json` — pas de base de données, parfait pour un seul apprenant.

---

## Prérequis

- **Python 3.12+** (ou **Docker** pour le mode 24/7)
- Un smartphone avec **Telegram**
- Une clé API **DeepSeek** (~5M tokens offerts à l'inscription)
- ~10 minutes

---

## Étape 1 — Bot Telegram

1. Ouvre Telegram, cherche **@BotFather**, envoie `/newbot`
2. Choisis un nom et un username finissant par `bot`
3. Copie le **token** (`123456789:ABC...`) → c'est `TELEGRAM_BOT_TOKEN`
4. Cherche **@userinfobot**, envoie `/start` → copie ton **Id** → c'est `TELEGRAM_CHAT_ID`
5. Envoie un message à ton nouveau bot (sinon il ne pourra pas t'écrire en premier)

## Étape 2 — Clé API DeepSeek

1. Va sur [platform.deepseek.com](https://platform.deepseek.com) → **API Keys** → **Create new secret key**
2. Copie la clé → c'est `DEEPSEEK_API_KEY`

## Étape 3 — Configuration

```bash
cd mentorpilot
cp .env.example .env
# édite .env : DEEPSEEK_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, LESSON_HOUR
```

---

## Lancement

### En local (Python)

```bash
cd mentorpilot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python orchestrator.py
```

### En Docker (24/7)

```bash
cd mentorpilot
docker compose up -d --build
docker compose logs -f mentor
```

Tu dois voir `Telegram bot started` puis `MentorPilot démarré`, et recevoir
**« 🤖 MentorPilot est en ligne ! »** sur Telegram.

---

## Utilisation au quotidien

Sur Telegram :

| Commande | Action |
|----------|--------|
| `/start` | Définir ton objectif et générer ta roadmap |
| `/plan` | Revoir ta roadmap complète |
| `/lesson` | Recevoir la leçon de l'étape en cours, à la demande |
| `/status` | Voir ta progression (%, série, étape) |
| `/next` | Marquer l'étape en cours comme terminée |
| `/restart` | Repartir sur un nouvel objectif |
| `/cancel` | Annuler l'action en cours |

**Boutons sous chaque leçon :**

| Bouton | Action |
|--------|--------|
| ✅ **Terminé** | Valide l'étape, met à jour la série, passe à la suite |
| ❓ **Une question** | Pose une question libre, le Tutor répond dans le contexte de l'étape |

Tu peux aussi écrire n'importe quelle question à tout moment : si une roadmap est active, le Tutor y répond.

---

## Personnalisation

- **Ton & format des leçons** → [`agents/tutor.py`](agents/tutor.py) (`LESSON_PROMPT`, `QUESTION_PROMPT`)
- **Structure de la roadmap** (nombre d'étapes, règles) → [`agents/planner.py`](agents/planner.py) (`SYSTEM_PROMPT`)
- **Heure de la leçon** → `LESSON_HOUR` dans `.env`

---

## Structure du projet

```
mentorpilot/
├── orchestrator.py        # point d'entrée — câble les agents, possède l'état
├── config.py              # configuration (variables d'env)
├── models.py              # LearningPlan, Milestone, Progress, AppState
├── state.py               # persistance JSON (load/save atomique)
├── agents/
│   ├── planner.py         # Agent 1 : objectif → roadmap
│   ├── scheduler.py       # Agent 2 : déclencheur quotidien
│   ├── tutor.py           # Agent 3 : leçon + Q/R
│   └── telegram_bot.py    # Agent 4 : interface apprenant
├── requirements.txt
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Coûts estimés

| Service | Coût | Notes |
|---------|------|-------|
| DeepSeek API | ~0,10 à 0,50 €/mois | 1 leçon/jour + quelques questions |
| VPS (optionnel) | ~5 €/mois | pour le mode 24/7 |
| Telegram | Gratuit | |

---

## Pistes pour la suite (hors MVP)

- **Code Reviewer** : l'apprenant colle son code → feedback automatique
- **Dashboard web** : visualiser la roadmap et la progression dans le navigateur
- **Multi-apprenants** : passer de `state.json` à Redis/SQLite indexé par `chat_id`
- **Quiz** : exercices auto-corrigés en fin d'étape
- **Ressources curatées** : ancrer la roadmap sur roadmap.sh plutôt que 100% généré
