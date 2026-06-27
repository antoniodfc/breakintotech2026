# Material — Documentation débutant pour BitMentor

Bienvenue ! Ce dossier rassemble tout ce qu'il faut pour **installer, comprendre et lancer**
le projet [BitMentor](../bitmentor/) quand on débute en tech.

Lis les guides **dans l'ordre** la première fois. Chaque guide est autonome et illustré
étape par étape.

---

## Parcours conseillé

On commence par préparer un **environnement Linux** (Ubuntu, dans une machine
virtuelle), puis on installe les outils **dedans**, et enfin on lance le projet.

| # | Guide | Ce que tu apprends | Durée |
|---|-------|--------------------|-------|
| 1 | [Prérequis matériel](01-prerequis-materiel.md) | Vérifier que ton PC est prêt (RAM, **disque libre**, virtualisation) | ~5 min |
| 2 | [La virtualisation & VirtualBox](02-virtualisation-virtualbox.md) | Comprendre les machines virtuelles + installer VirtualBox | ~15 min |
| 3 | [Ubuntu : OS & ISO](03-ubuntu-os-et-iso.md) | Ce qu'est un système d'exploitation + télécharger Ubuntu | ~10 min* |
| 4 | [Installer la VM Ubuntu](04-installer-vm-ubuntu.md) | Créer la machine virtuelle et installer Ubuntu pas à pas | ~30–45 min |
| 5 | [GitHub : compte + cloner le repo](05-github-compte-et-clone.md) | Récupérer le **code** du projet (dans Ubuntu) | ~15 min |
| 6 | [Installer Docker](06-installation-docker.md) | Préparer Ubuntu à faire tourner l'app | ~10 min |
| 7 | [Installer & configurer Telegram](07-installation-telegram.md) | Créer ton bot, remplir le `.env` et **lancer BitMentor** | ~10 min |
| 8 | [Glossaire débutant](08-glossaire.md) | Comprendre tous les mots du projet | à consulter au besoin |

> *\* hors temps de téléchargement de l'ISO (~5–6 Go).*

> **Suis-les dans cet ordre.** Les guides 1→4 montent ton **environnement Ubuntu** ;
> à partir du guide 5, **tout se passe dans Ubuntu** (Git, Docker, le projet). C'est le
> guide Telegram (7) qui **remplit le `.env` et lance le projet** à la fin.

> **Sur un Mac à puce Apple (M1–M4) :** VirtualBox est instable — **contacte-nous
> avant de commencer** pour la marche à suivre adaptée (le parcours ci-dessous cible
> Windows).

---

## Dans quel ordre faire les choses ?

```
1→4. Monter l'environnement
     Prérequis OK ─► VirtualBox ─► ISO Ubuntu ─► VM Ubuntu installée
            │
            ▼   ★ à partir d'ici, TOUT se passe dans Ubuntu ★
5. GitHub : compte + clone   ──►   tu as le CODE du projet
            │
            ▼
6. Docker : installer        ──►   Ubuntu peut LANCER l'app
            │
            ▼
7. Telegram : créer le bot + récupérer les clés
            │
            ▼
   Remplir le .env   (clés Telegram + DeepSeek)
            │
            ▼
   docker compose up -d   (depuis le dossier bitmentor/)
            │
            ▼
   /start sur Telegram
```

> **Bloqué sur un mot ?** Ouvre le [glossaire](08-glossaire.md) : tout y est expliqué
> avec des images simples (un terminal, un dépôt, un conteneur…).

---

## Checklist avant de lancer le projet

- [ ] Mon PC passe les **prérequis** (RAM, 50 Go libres, virtualisation activée)
- [ ] **VirtualBox** est installé
- [ ] Ma **VM Ubuntu** est installée, à jour, et je sais ouvrir son terminal
- [ ] J'ai un compte **GitHub** et j'ai **cloné** le repo (dans Ubuntu)
- [ ] **Docker** est installé dans Ubuntu (`docker run hello-world` fonctionne)
- [ ] J'ai créé mon **bot Telegram** avec @BotFather → j'ai mon `TELEGRAM_BOT_TOKEN`
- [ ] J'ai récupéré mon `TELEGRAM_CHAT_ID` avec @userinfobot
- [ ] J'ai ma clé **DeepSeek** (`DEEPSEEK_API_KEY`)
- [ ] J'ai copié `.env.example` en `.env` et rempli mes clés (+ `TZ`)
- [ ] J'ai lancé `docker compose up -d --build` dans le dossier `bitmentor/`
- [ ] J'ai reçu « 🤖 BitMentor est en ligne ! » sur Telegram
