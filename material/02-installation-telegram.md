# 💬 Guide 2 — Installer Telegram et configurer ton bot

MentorPilot te parle **via Telegram** : c'est ton interface. Tu vas créer un **bot**
(un compte automatisé piloté par le code) et récupérer **3 informations** à coller
dans le fichier `.env`.

À la fin de ce guide tu auras :

| Variable | Ce que c'est | Exemple de format |
|----------|--------------|-------------------|
| `TELEGRAM_BOT_TOKEN` | La clé secrète de ton bot | `8123456789:AAH...long...` |
| `TELEGRAM_CHAT_ID` | Ton identifiant perso (pour que le bot t'écrive) | `7042123456` |
| `DEEPSEEK_API_KEY` | La clé de l'IA qui rédige les leçons | `sk-...` |

> 🧠 Un *token*, une *clé API* ? Voir le [glossaire](04-glossaire.md#token--cle-api).

---

## Étape 1 — Installer Telegram

1. Sur ton **téléphone** : installe **Telegram** depuis l'App Store (iPhone) ou
   le Play Store (Android), puis crée ton compte avec ton numéro.
2. *(Optionnel mais pratique)* installe aussi **Telegram Desktop** sur ton ordi :
   https://desktop.telegram.org — ça permet de copier-coller les clés facilement.

---

## Étape 2 — Créer ton bot avec @BotFather

**@BotFather** est le bot officiel de Telegram qui sert à créer d'autres bots.

1. Dans la barre de recherche Telegram, tape **`BotFather`** et ouvre celui avec la
   **coche bleue** ✅ (compte vérifié).
2. Clique sur **Démarrer** (ou envoie `/start`).
3. Envoie la commande :
   ```
   /newbot
   ```
4. Il te demande un **nom** (affiché) — ex : `Mon Mentor IA`
5. Puis un **username** qui doit **finir par `bot`** — ex : `mon_mentor_2026_bot`
   *(s'il est déjà pris, essaie une variante)*
6. 🎉 BotFather te répond avec un message contenant ton **token** :
   ```
   Use this token to access the HTTP API:
   8123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

![Conversation BotFather après /newbot montrant le token du bot](img/botfather-newbot.png)

➡️ **Copie ce token** : c'est ton **`TELEGRAM_BOT_TOKEN`**.

> 🔒 **Ne partage JAMAIS ce token** publiquement. Quiconque l'a peut contrôler ton bot.
> Si tu le divulgues par erreur, renvoie `/revoke` à BotFather pour en générer un nouveau.

---

## Étape 3 — Récupérer ton `TELEGRAM_CHAT_ID`

Le bot a besoin de savoir **à qui** envoyer les messages : c'est ton *chat ID*.

**Méthode simple — @userinfobot :**

1. Cherche **`userinfobot`** dans Telegram et ouvre-le.
2. Envoie `/start`.
3. Il te répond avec tes infos, dont :
   ```
   Id: 7042123456
   ```

![Réponse de userinfobot affichant l'Id du compte](img/userinfobot-id.png)

➡️ Le nombre après `Id:` est ton **`TELEGRAM_CHAT_ID`**.

> ℹ️ **Bon à savoir** : un ID de personne est un nombre **positif**.
> Pour un **groupe** il serait **négatif** (ex : `-1001234...`). Ici on utilise ton
> chat perso, donc un nombre positif.

---

## Étape 4 — Réveiller ton bot

Un bot Telegram **ne peut pas** écrire à quelqu'un en premier tant que cette personne
ne lui a pas parlé au moins une fois.

1. Dans Telegram, cherche le **username de TON bot** (ex : `mon_mentor_2026_bot`).
2. Ouvre-le et clique sur **Démarrer** (ou envoie n'importe quel message).

![Bouton « Démarrer » sous la conversation du bot](img/bot-start-button.png)

C'est tout — maintenant le bot a le droit de t'écrire. ✅

---

## Étape 5 — Obtenir ta clé DeepSeek (l'IA)

C'est l'IA qui **rédige les roadmaps et les leçons**.

1. Va sur **https://platform.deepseek.com** et crée un compte (≈ 5 M de tokens
   offerts à l'inscription, largement suffisant pour tester).
2. Menu **API Keys** → **Create new secret key**.
3. **Copie** la clé immédiatement (format `sk-...`) — elle ne s'affiche qu'une fois.

![Page API Keys de DeepSeek avec le bouton de création de clé](img/deepseek-apikey.png)

➡️ C'est ta **`DEEPSEEK_API_KEY`**.

---

## Étape 6 — Remplir le fichier `.env`

Dans le dossier `mentorpilot/`, crée ton fichier de configuration à partir du modèle :

```bash
cd mentorpilot
cp .env.example .env
```

> 🪟 **Sur Windows** : `cp` fonctionne dans **PowerShell** et **Git Bash**. Dans
> l'invite de commandes **CMD**, utilise plutôt `copy .env.example .env`.

Ouvre `.env` (dans ton éditeur de code, ex. VS Code) et remplace les valeurs
d'exemple par **tes vraies clés** :

> ⚠️ **Piège Windows** : n'édite **pas** le `.env` avec le **Bloc-notes** —
> il risque de l'enregistrer sous le nom `.env.txt` (avec une extension cachée),
> et l'app ne le trouvera plus. Utilise **VS Code** (ou, dans le Bloc-notes,
> choisis « Type : Tous les fichiers » et nomme bien `.env`). Le fichier doit
> s'appeler **exactement `.env`**, sans rien après.

```ini
DEEPSEEK_API_KEY=sk-ta_vraie_cle_deepseek
TELEGRAM_BOT_TOKEN=8123456789:AAH...ton_vrai_token
TELEGRAM_CHAT_ID=7042123456
LESSON_HOUR=9
```

![Fichier .env rempli ouvert dans VS Code](img/env-rempli.png)

- `LESSON_HOUR` = l'heure (0–23, heure locale) où le bot t'envoie la leçon du jour.
  `9` = 9 h du matin.

> 🔒 **Le fichier `.env` ne doit jamais être partagé ni envoyé sur GitHub.**
> Bonne nouvelle : il est déjà protégé par le `.gitignore` du projet (voir
> [glossaire → .gitignore](04-glossaire.md#gitignore)).

---

## Étape 7 — Lancer et vérifier

```bash
docker compose up -d --build
docker compose logs -f mentor
```

Tu dois voir dans les logs :

```
Telegram bot started
MentorPilot démarré. En attente d'événements...
```

…et recevoir **« 🤖 MentorPilot est en ligne ! »** dans ta conversation Telegram. 🎉

<!-- 📸 À insérer plus tard : ![Message « MentorPilot est en ligne ! » reçu sur Telegram](img/mentorpilot-online.png) -->

Envoie alors **`/start`** à ton bot pour définir ton objectif et générer ta roadmap.

![Résultat de /start : objectif et roadmap générée](img/start-roadmap.png)

---

## 🆘 Problèmes fréquents

| Symptôme | Cause | Solution |
|----------|-------|----------|
| `InvalidToken ... was rejected` | Token faux ou resté en placeholder | Recopie le vrai token, puis `docker compose up -d --force-recreate` |
| Le bot démarre mais ne t'écrit pas | Tu n'as pas « démarré » ton bot | Ouvre ton bot, clique **Démarrer** (étape 4) |
| `TELEGRAM_CHAT_ID manquant ou invalide` | ID vide ou non numérique | Remets le nombre donné par @userinfobot |
| Les leçons n'arrivent pas à l'heure | Mauvais `LESSON_HOUR` ou fuseau | Mets l'heure locale (0–23) et recrée le conteneur |

➡️ **Suite : [GitHub : compte + cloner un repo](03-github-compte-et-clone.md)**
