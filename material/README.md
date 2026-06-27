# Material — Documentation débutant pour BitMentor

Bienvenue ! Ce dossier rassemble tout ce qu'il faut pour **installer, comprendre et lancer**
le projet [BitMentor](../bitmentor/) quand on débute en tech.

Lis les guides **dans l'ordre** la première fois. Chaque guide est autonome et illustré
étape par étape.

---

## Parcours conseillé

| # | Guide | Ce que tu apprends | Durée |
|---|-------|--------------------|-------|
| 1 | [GitHub : compte + cloner le repo](01-github-compte-et-clone.md) | Récupérer le **code** du projet sur ton ordinateur | ~15 min |
| 2 | [Installer Docker](02-installation-docker.md) | Préparer ta machine à faire tourner l'app | ~10 min |
| 3 | [Installer & configurer Telegram](03-installation-telegram.md) | Créer ton bot, remplir le `.env` et **lancer BitMentor** | ~10 min |
| 4 | [Glossaire débutant](04-glossaire.md) | Comprendre tous les mots du projet | à consulter au besoin |

> 👉 **Suis-les dans cet ordre.** Chaque guide suppose le précédent fait : on récupère
> d'abord le code (1), puis on installe Docker (2), et c'est le guide Telegram (3) qui
> **remplit le `.env` et lance le projet** à la fin.

---

## Dans quel ordre faire les choses ?

```
1. GitHub : compte + clone   ──►   tu as le CODE du projet
            │
            ▼
2. Docker : installer        ──►   ta machine peut LANCER l'app
            │
            ▼
3. Telegram : créer le bot + récupérer les clés
            │
            ▼
   Remplir le .env   (clés Telegram + DeepSeek)
            │
            ▼
   docker compose up -d   (depuis le dossier bitmentor/)
            │
            ▼
   /start sur Telegram 🎉
```

> **Bloqué sur un mot ?** Ouvre le [glossaire](04-glossaire.md) : tout y est expliqué
> avec des images simples (un terminal, un dépôt, un conteneur…).

---

## Checklist avant de lancer le projet

- [ ] J'ai un compte **GitHub** et j'ai **cloné** le repo
- [ ] **Docker Desktop** est installé et la baleine 🐳 est allumée
- [ ] J'ai créé mon **bot Telegram** avec @BotFather → j'ai mon `TELEGRAM_BOT_TOKEN`
- [ ] J'ai récupéré mon `TELEGRAM_CHAT_ID` avec @userinfobot
- [ ] J'ai ma clé **DeepSeek** (`DEEPSEEK_API_KEY`)
- [ ] J'ai copié `.env.example` en `.env` et rempli mes 3 clés
- [ ] J'ai lancé `docker compose up -d --build` dans le dossier `bitmentor/`
- [ ] J'ai reçu « 🤖 BitMentor est en ligne ! » sur Telegram
