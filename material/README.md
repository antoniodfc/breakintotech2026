# 📚 Material — Documentation débutant pour MentorPilot

Bienvenue ! Ce dossier rassemble tout ce qu'il faut pour **installer, comprendre et lancer**
le projet [MentorPilot](../mentorpilot/) quand on débute en tech.

Lis les guides **dans l'ordre** la première fois. Chaque guide est autonome et illustré
étape par étape.

---

## 🗺️ Parcours conseillé

| # | Guide | Ce que tu apprends | Durée |
|---|-------|--------------------|-------|
| 1 | [Installer Docker](01-installation-docker.md) | Faire tourner l'app sans rien installer d'autre | ~10 min |
| 2 | [Installer & configurer Telegram](02-installation-telegram.md) | Créer ton bot et récupérer tes clés | ~10 min |
| 3 | [GitHub : compte + cloner un repo](03-github-compte-et-clone.md) | Récupérer le code sur ton ordinateur | ~15 min |
| 4 | [Glossaire débutant](04-glossaire.md) | Comprendre tous les mots du projet | à consulter au besoin |

---

## 🎯 Dans quel ordre faire les choses ?

```
1. Créer un compte GitHub  ─┐
2. Cloner le repo           ├─►  3. Installer Docker
3. Installer Telegram       │         │
   + créer le bot           │         ▼
   + récupérer les clés ────┘    4. Remplir le .env
                                       │
                                       ▼
                                 docker compose up -d
                                       │
                                       ▼
                                 /start sur Telegram 🎉
```

> 💡 **Bloqué sur un mot ?** Ouvre le [glossaire](04-glossaire.md) : tout y est expliqué
> avec des images simples (un terminal, un dépôt, un conteneur…).

---

## ✅ Checklist avant de lancer le projet

- [ ] J'ai un compte **GitHub** et j'ai **cloné** le repo
- [ ] **Docker Desktop** est installé et la baleine 🐳 est allumée
- [ ] J'ai créé mon **bot Telegram** avec @BotFather → j'ai mon `TELEGRAM_BOT_TOKEN`
- [ ] J'ai récupéré mon `TELEGRAM_CHAT_ID` avec @userinfobot
- [ ] J'ai ma clé **DeepSeek** (`DEEPSEEK_API_KEY`)
- [ ] J'ai copié `.env.example` en `.env` et rempli mes 3 clés
- [ ] J'ai lancé `docker compose up -d --build` dans le dossier `mentorpilot/`
- [ ] J'ai reçu « 🤖 MentorPilot est en ligne ! » sur Telegram
