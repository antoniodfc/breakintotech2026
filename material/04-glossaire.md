# Glossaire débutant — BitMentor

Tous les mots et concepts du projet, expliqués simplement. Classés par thème.
Utilise `Cmd + F` pour chercher un mot.

- [1. Les bases (tech & code)](#1-les-bases-tech--code)
- [2. Git & GitHub](#2-git--github)
- [3. Docker](#3-docker)
- [4. Telegram & bots](#4-telegram--bots)
- [5. IA & API (DeepSeek)](#5-ia--api-deepseek)
- [6. Les concepts propres à BitMentor](#6-les-concepts-propres-à-bitmentor)

---

## 1. Les bases (tech & code)

### <a id="terminal-ou-ligne-de-commande"></a>Terminal (ou « ligne de commande », ou « CLI »)
Une fenêtre où tu tapes des **commandes texte** au lieu de cliquer, puis tu appuies sur
**Entrée**. C'est là qu'on lance Git, Docker, etc. **CLI** = *Command Line Interface*,
c'est le même outil.
Le nom et la façon de l'ouvrir changent selon ton système :

| Système | Appli à ouvrir | Comment l'ouvrir |
|---------|----------------|------------------|
| 🍎 Mac | **Terminal** | `Cmd + Espace` → « Terminal » → `Entrée` |
| 🪟 Windows | **PowerShell** (ou Terminal Windows) | Menu Démarrer → « PowerShell » → `Entrée` |
| 🐧 Linux | **Terminal** | `Ctrl + Alt + T`, ou cherche « Terminal » |

Exemple de commande : `ls` (lister les fichiers), `cd` (changer de dossier).
Une commande **« En CLI »** = une commande à taper dans cette fenêtre.

### Commande
Une instruction qu'on tape dans le terminal. Structure typique :
`outil action options`. Ex : `docker compose up -d` → outil `docker`, action `compose up`,
option `-d`.

### `cd` / `ls`
- `cd nom_du_dossier` → **entre** dans un dossier (« change directory »).
- `cd ..` → remonte d'un dossier.
- `ls` → **liste** ce qu'il y a dans le dossier courant.

### Chemin (path)
L'adresse d'un fichier ou dossier. Ex : `bitmentor/agents/planner.py`.
`~` = ton dossier personnel (ex : `/Users/peco3k`).

### Python
Le **langage de programmation** dans lequel BitMentor est écrit. Les fichiers
finissent par `.py`. Tu n'as **pas besoin de l'installer** ici : Docker s'en charge.

### Librairie / dépendance
Du code déjà écrit par d'autres, que le projet réutilise. Elles sont listées dans
[`requirements.txt`](../bitmentor/requirements.txt) (ex : `python-telegram-bot`).
« Installer les dépendances » = télécharger ces briques.

### Variable d'environnement
Un réglage fourni **à l'extérieur** du code, pour ne pas écrire les secrets en dur dans
les fichiers. Ex : `TELEGRAM_BOT_TOKEN`. Elles sont stockées dans le fichier **`.env`**.

### `.env`
Le fichier texte qui contient **tes réglages et tes secrets** (clés, token).
Format `CLE=valeur`, une par ligne. **Jamais partagé.**

### `.env.example`
Un **modèle** du `.env`, **sans secrets** (juste des valeurs d'exemple). Il est, lui,
partagé sur GitHub pour montrer quelles variables remplir. On le copie :
`cp .env.example .env`.

### <a id="token--cle-api"></a>Token / Clé API
Une **longue chaîne secrète** qui sert de mot de passe pour utiliser un service.
- `TELEGRAM_BOT_TOKEN` → prouve que c'est bien ton bot.
- `DEEPSEEK_API_KEY` → prouve que tu as le droit d'utiliser l'IA.
À garder secret. Si fuité, on le **révoque** (annule) et on en génère un nouveau.

### JSON
Un format texte pour **stocker des données structurées**, lisible par l'humain et la
machine. BitMentor enregistre ta progression dans un fichier `state.json`. Exemple :
```json
{ "goal": "devenir développeur web", "level": "débutant" }
```

### Log (journal)
Les **messages** qu'affiche un programme pendant qu'il tourne, pour dire ce qu'il fait
(ou quelle erreur survient). On les lit avec `docker compose logs -f bitmentor`.

### Bug / Erreur / Traceback
- **Bug** : un comportement non voulu.
- **Traceback** : le « rapport d'erreur » de Python qui montre **où** ça a planté
  (la longue liste de `File ".../...py", line X`). On lit surtout la **dernière** ligne.

---

## 2. Git & GitHub

### <a id="git"></a>Git
L'outil installé **sur ton ordinateur** qui suit l'**historique** de ton code : qui a
changé quoi, et quand. Permet de revenir en arrière.

### GitHub
Le **site web** qui héberge le code en ligne (https://github.com). C'est la version
« cloud » + partage de Git. *(Git = l'outil ; GitHub = le site.)*

### Repository (repo / dépôt)
Un **projet** versionné par Git. C'est un dossier suivi par Git, avec tout son
historique. Ex : `breakintotech2026`.

### Cloner (`git clone`)
**Télécharger une copie complète** d'un repo (code + historique) sur ton ordinateur :
```bash
git clone https://github.com/antoniodfc/breakintotech2026.git
```

### Commit
Une **photo enregistrée** de ton code à un instant donné, avec un message décrivant le
changement. C'est l'unité de base de l'historique.
```bash
git commit -m "Ajoute la documentation débutant"
```

### Branche (branch)
Une **ligne de travail parallèle**. `main` est la branche principale. On crée d'autres
branches pour développer une nouveauté sans casser `main`.

### `git add` / `git push` / `git pull`
- `git add` → **prépare** les fichiers à enregistrer dans le prochain commit.
- `git push` → **envoie** tes commits locaux sur GitHub.
- `git pull` → **récupère** les derniers changements depuis GitHub.

### <a id="gitignore"></a>`.gitignore`
Un fichier qui liste ce que Git doit **ignorer** (ne jamais enregistrer). On y met les
secrets et les fichiers générés. Dans ce projet il ignore notamment :
`.env` (secrets), `state.json` (données), `__pycache__/` et `.venv/` (fichiers Python).
C'est ce qui empêche tes clés de partir sur GitHub.

### <a id="https-vs-ssh"></a>HTTPS vs SSH
Deux façons de se connecter à GitHub pour cloner/pousser :
- **HTTPS** : juste une URL (`https://...`). Simple → **à privilégier pour débuter**.
- **SSH** : plus rapide à l'usage mais demande de configurer une **clé SSH**. Plus tard.

### <a id="personal-access-token-pat"></a>Personal Access Token (PAT)
Un **jeton** qui remplace ton mot de passe pour `git push` en HTTPS (GitHub n'accepte
plus le mot de passe classique). Tu le crées dans GitHub → *Settings → Developer
settings → Personal access tokens*, et tu le colles quand le terminal demande un mot
de passe.

---

## 3. Docker

### <a id="docker"></a>Docker
Un outil qui emballe une application avec **tout son environnement** (Python, librairies,
réglages) dans une boîte standardisée. Avantage : « ça marche pareil partout », sans rien
installer à la main.

### Image
Le **modèle figé** de l'application (comme un plan ou un gâteau emballé). On la
construit à partir du **Dockerfile**. Elle ne tourne pas toute seule.

### Conteneur (container)
Une **instance qui tourne**, créée à partir d'une image (le gâteau qu'on sort du paquet
et qu'on mange). C'est dans le conteneur que BitMentor s'exécute réellement.

### Dockerfile
La **recette** pour construire l'image : « pars de Python 3.12, installe les
dépendances, copie le code, lance `orchestrator.py` ». Voir
[`bitmentor/Dockerfile`](../bitmentor/Dockerfile).

### docker-compose / `docker-compose.yml`
Un outil pour **décrire et lancer** un (ou plusieurs) conteneur(s) avec une seule
commande, en lisant le fichier `docker-compose.yml` (qui dit quel `.env` utiliser, quels
dossiers monter, redémarrer en cas de crash, etc.).

### Volume
Un **dossier partagé** entre ton ordinateur et le conteneur, pour **garder les données**
même si le conteneur est supprimé. Ici, le dossier `data/` garde ton `state.json`
(ta progression) entre deux redémarrages.

### <a id="commandes-docker-utiles"></a>Commandes Docker utiles
| Commande | Ce qu'elle fait |
|----------|-----------------|
| `docker compose up -d --build` | Construit l'image et lance l'app en arrière-plan |
| `docker compose logs -f bitmentor` | Affiche les logs en direct |
| `docker compose down` | Arrête et supprime le conteneur |
| `docker compose up -d --force-recreate` | Recrée le conteneur (utile après avoir modifié `.env`) |
| `docker ps` | Liste les conteneurs en cours d'exécution |

### « detached » (`-d`)
L'option `-d` lance l'app **en arrière-plan** : elle continue de tourner et tu récupères
ton terminal (au lieu de rester « bloqué » à regarder les logs).

### <a id="wsl-2-windows"></a>WSL 2 (Windows uniquement)
**Windows Subsystem for Linux 2** : une mini-machine Linux intégrée à Windows. Docker
Desktop s'en sert pour faire tourner les conteneurs sur Windows. Docker l'installe
automatiquement ; si besoin on le met à jour avec `wsl --update` dans PowerShell. Les
utilisateurs Mac et Linux n'ont pas à s'en soucier.

---

## 4. Telegram & bots

### Bot
Un **compte automatisé** sur Telegram, piloté par du code. BitMentor **est** un bot :
tu lui parles, il te répond.

### @BotFather
Le **bot officiel** de Telegram qui sert à **créer et configurer** d'autres bots
(générer le token, changer le nom, etc.).

### @userinfobot
Un bot pratique qui te **donne ton identifiant** Telegram (`TELEGRAM_CHAT_ID`) quand tu
lui envoies `/start`.

### Chat ID (`TELEGRAM_CHAT_ID`)
Ton **identifiant numérique** de conversation. Le bot en a besoin pour savoir **à qui**
envoyer les leçons. Positif pour une personne, négatif pour un groupe.

### Commande Telegram (slash command)
Un message qui commence par `/`, interprété comme une **action**. Dans BitMentor :
| Commande | Effet |
|----------|-------|
| `/start` | Définir ton objectif et générer la roadmap |
| `/plan` | Revoir ta roadmap complète |
| `/lesson` | Recevoir tout de suite la leçon de l'étape en cours |
| `/status` | Voir ta progression (%, série, étape) |
| `/next` | Marquer l'étape en cours comme terminée |
| `/restart` | Repartir sur un nouvel objectif |
| `/cancel` | Annuler l'action en cours |

### Webhook vs Polling
Deux façons pour un bot de **recevoir** les messages.
- **Polling** : le bot **demande régulièrement** « du nouveau ? » (`getUpdates`). C'est
  ce qu'utilise BitMentor — voir la ligne `getUpdates` dans les logs.
- **Webhook** : Telegram **prévient** le bot dès qu'un message arrive (plus avancé).

---

## 5. IA & API (DeepSeek)

### IA / LLM (Large Language Model)
Un **modèle d'intelligence artificielle** entraîné à comprendre et générer du texte.
Ici, c'est lui qui **rédige les roadmaps et les leçons**. DeepSeek en est un.

### DeepSeek
Le **fournisseur d'IA** utilisé par le projet. On l'appelle via une **API** avec la clé
`DEEPSEEK_API_KEY`. Son interface est compatible avec celle d'OpenAI.

### API (Application Programming Interface)
Une **porte d'entrée** qui permet à un programme d'en utiliser un autre à distance.
BitMentor envoie ta demande à l'**API de DeepSeek** et reçoit le texte généré en retour.

### Token (au sens IA)
Mot à double sens ! Côté IA, un *token* est un **morceau de mot** (≈ ¾ d'un mot).
Les modèles facturent au nombre de tokens. Rien à voir avec le *token secret* de Telegram.

### Prompt
Le **texte d'instruction** envoyé à l'IA pour orienter sa réponse (ton, format, rôle).
Dans le projet, les prompts vivent dans
[`agents/planner.py`](../bitmentor/agents/planner.py) et
[`agents/tutor.py`](../bitmentor/agents/tutor.py).

---

## 6. Les concepts propres à BitMentor

### Agent
Un **module spécialisé** qui s'occupe d'**une** responsabilité. BitMentor est une
**flotte de 4 agents** qui collaborent (voir tableau ci-dessous). C'est une façon
d'organiser le code proprement.

| Agent | Fichier | Rôle |
|-------|---------|------|
| **Planner** | [`agents/planner.py`](../bitmentor/agents/planner.py) | Objectif + niveau → génère la roadmap (IA) |
| **Scheduler** | [`agents/scheduler.py`](../bitmentor/agents/scheduler.py) | Déclenche la leçon chaque jour à heure fixe |
| **Tutor** | [`agents/tutor.py`](../bitmentor/agents/tutor.py) | Rédige la leçon et répond aux questions (IA) |
| **Telegram bot** | [`agents/telegram_bot.py`](../bitmentor/agents/telegram_bot.py) | L'interface avec toi (commandes, boutons) |

### Orchestrateur (Orchestrator)
Le **chef d'orchestre** : le point d'entrée
([`orchestrator.py`](../bitmentor/orchestrator.py)) qui **démarre et relie** tous les
agents, détient l'état, et fait circuler l'information entre eux.

### Planner
L'agent qui transforme ton **objectif + niveau** en une **roadmap** structurée, grâce à
l'IA. Tu peux la valider ou demander un ajustement.

### Tutor
L'agent qui **rédige la leçon** de l'étape en cours et **répond à tes questions**, en
restant dans le contexte de ton étape, grâce à l'IA.

### Scheduler
L'agent « réveil » : à l'heure définie par `LESSON_HOUR`, il déclenche l'envoi de la
**leçon du jour**. Il évite les doublons (pas deux leçons le même jour).

### Roadmap / LearningPlan
Ton **plan d'apprentissage personnalisé** : objectif + niveau + une liste d'**étapes**
(milestones). Représenté par la classe `LearningPlan` dans
[`models.py`](../bitmentor/models.py).

### Milestone (étape / jalon)
**Une étape** de la roadmap : un titre, un concept à apprendre, une durée estimée, et un
statut « fait / pas fait ». Tu avances milestone par milestone.

### Progress (progression)
Le **suivi de ton avancement** : étape en cours, étapes terminées, **streak** (série) et
pourcentage de complétion.

### Streak (série)
Le **nombre d'étapes validées d'affilée** — un petit côté « jeu » pour rester motivé.
Il augmente à chaque `/next` (étape terminée).

### État (State) / `state.json`
La **mémoire** de l'application : ta roadmap + ta progression, sauvegardées dans le
fichier `state.json`. Pas de base de données — un simple fichier, parfait pour un seul
apprenant. (Stocké dans un **volume** Docker pour survivre aux redémarrages.)

### Human-in-the-loop (« humain dans la boucle »)
Le principe où **tu valides** les décisions clés : l'IA propose une roadmap, mais **rien
n'avance sans ton **. Tu gardes le contrôle.

### Callback
Une fonction qu'on **branche** pour être appelée quand un événement se produit (ex :
« quand l'utilisateur valide la roadmap, fais ceci »). L'orchestrateur relie les agents
entre eux avec des callbacks.

### Asynchrone (async / `await`)
Une façon de programmer où le programme peut **gérer plusieurs choses sans se bloquer**
(écouter Telegram **et** attendre le scheduler en même temps). Les mots-clés Python sont
`async` et `await`. Pas besoin de tout comprendre pour utiliser le projet.

---

## Pour aller plus loin

- Le [README du projet](../bitmentor/README.md) — vue d'ensemble et schéma d'architecture
- [Guide GitHub](01-github-compte-et-clone.md) · [Guide Docker](02-installation-docker.md) · [Guide Telegram](03-installation-telegram.md)

> Un terme manque ? Ajoute-le ici, c'est un document vivant !
