# Guide 9 — Débugger : la méthode (et bien demander de l'aide)

> À consulter **dès que tu es bloqué**, à n'importe quelle étape du parcours.

Un **bug**, ce n'est pas un échec : c'est le quotidien **normal** de tous les
développeurs, même les plus expérimentés. Ce qui fait la différence, ce n'est pas
« ne jamais avoir de bug » — c'est **savoir s'y prendre** pour le résoudre.

Le but de ce guide n'est pas de te donner « la réponse ». C'est de te rendre
**autonome** : te donner la **méthode** que tu réutiliseras toute ta carrière. Un LLM
(ChatGPT, Claude, DeepSeek…) est un excellent **outil** dans cette méthode — pas un
remplaçant de ta réflexion.

---

## 1. Débugger, c'est une enquête (le cheminement)

Un bug a **toujours une cause**. Il n'y a pas de magie. On la trouve par une démarche
proche de la méthode scientifique :

```
   ┌─────────────────────────────────────────────┐
   │  1. REPRODUIRE   — refaire le bug à volonté  │
   │           │                                  │
   │           ▼                                  │
   │  2. LIRE l'erreur — surtout la DERNIÈRE ligne│
   │           │                                  │
   │           ▼                                  │
   │  3. HYPOTHÈSE   — « je pense que X, parce que Y » │
   │           │                                  │
   │           ▼                                  │
   │  4. TESTER     — changer UNE seule chose     │
   │           │                                  │
   │           ▼                                  │
   │  5. VÉRIFIER   — résolu ? ───non──► retour 3 │
   │           │ oui                              │
   │           ▼                                  │
   │        Compris + noté                        │
   └─────────────────────────────────────────────┘
```

Les 4 réflexes qui changent tout :

- **Lis le message d'erreur.** La cause y est **presque toujours** écrite. Les débutants
  paniquent et ne le lisent pas — c'est l'erreur n°1. Va à la **dernière ligne** du
  message (voir [glossaire → Traceback](08-glossaire.md#bug--erreur--traceback)).
- **Change UNE chose à la fois.** Si tu modifies cinq trucs d'un coup, tu ne sauras pas
  lequel a corrigé (ou aggravé) le problème.
- **Isole.** Réduis au **plus petit cas** qui reproduit le bug. Plus c'est petit, plus
  la cause saute aux yeux.
- **Note ce que tu as essayé.** Ça t'évite de tourner en rond, et c'est précieux quand
  tu demandes de l'aide.

> **Reformuler le problème à voix haute** (ou à un collègue, ou à un canard en
> plastique — le fameux *rubber duck debugging*) résout une bonne partie des bugs
> avant même d'avoir cherché.

---

## 2. Où chercher — et dans quel ordre

| Ordre | Source | Pour quoi | Fiabilité |
|-------|--------|-----------|-----------|
| 1 | **Le message d'erreur** | La cause est souvent dedans | Élevée |
| 2 | **La doc officielle** | La référence qui fait autorité | Élevée |
| 3 | **StackOverflow / moteur de recherche** | Quelqu'un a déjà eu ton erreur | Bonne |
| 4 | **Un LLM** (ChatGPT/Claude/DeepSeek) | Explication rapide, sur mesure | À vérifier |
| 5 | **Un humain** (l'accompagnement BIT) | Quand tu as déjà cherché | Élevée |

> Astuce recherche : **colle le message d'erreur** (la dernière ligne) dans le moteur de
> recherche, entre guillemets, **sans** les parties personnelles (ton nom de fichier, ton
> chemin). Ex : `"Cannot connect to the Docker daemon"`.

### Liens utiles (à mettre en favoris)

**Général / méthode**
- [StackOverflow](https://stackoverflow.com/) — Q/R de développeurs (surtout en anglais)
- [DevDocs](https://devdocs.io/) — toutes les docs officielles réunies, cherchables
- [explainshell](https://explainshell.com/) — explique **chaque morceau** d'une commande shell

**Les outils du parcours**
- Linux / Ubuntu : [doc Ubuntu](https://help.ubuntu.com/) · [Ask Ubuntu](https://askubuntu.com/)
- Terminal / commandes : [explainshell](https://explainshell.com/)
- Git : [doc Git](https://git-scm.com/doc) · [livre Pro Git (FR, gratuit)](https://git-scm.com/book/fr/v2)
- GitHub : [docs GitHub (FR)](https://docs.github.com/fr)
- Docker : [docs Docker](https://docs.docker.com/) · [référence Compose](https://docs.docker.com/compose/)
- VirtualBox : [manuel VirtualBox](https://www.virtualbox.org/manual/)
- Python : [doc Python (FR)](https://docs.python.org/fr/3/)
- Telegram bots : [Bot API](https://core.telegram.org/bots/api)
- DeepSeek : [docs API DeepSeek](https://api-docs.deepseek.com/)

---

## 3. Bien demander à un LLM (le template)

Un LLM répond **aussi bien que ta question est précise**. « ça marche pas, aide-moi »
donne une réponse inutile. Donne-lui le **contexte**, ton **objectif**, l'**erreur
exacte** et ce que tu as **déjà essayé**.

> ⚠️ **Sécurité — non négociable :** ne colle **JAMAIS** de secret dans un LLM (ni dans
> une recherche web) : pas de `TELEGRAM_BOT_TOKEN`, pas de `DEEPSEEK_API_KEY`, pas le
> contenu de ton `.env`. Remplace toujours par `XXXX`. Un secret collé quelque part est
> un secret **fuité**.

Copie-colle ce modèle et remplis les `[...]` :

```
Je suis grand débutant en tech, sois pédagogue et concis.

Contexte : je travaille dans [Ubuntu, dans une VM VirtualBox].
Mon objectif : [ce que j'essaie de faire].
La commande / l'action exacte : [ce que j'ai tapé ou cliqué].
Ce que j'attendais : [le résultat espéré].
Ce qui se passe à la place : [le comportement réel].

Message d'erreur EXACT (copié-collé, SANS aucun secret) :
[colle ici le message — surtout la dernière ligne]

Mon environnement : [ex : Ubuntu 24.04, Docker 27.x].
Ce que j'ai déjà essayé : [tes tentatives].

Explique-moi d'abord la CAUSE simplement, puis la solution étape par étape,
et enfin comment éviter que ça se reproduise.
```

Pourquoi ce template marche : il force le LLM à **expliquer la cause** (tu apprends),
pas seulement à te donner une commande à copier (tu restes dépendant).

---

## 4. Après la réponse : garde ton esprit critique

Un LLM peut se tromper avec **aplomb** (il « invente » parfois des commandes ou des
options qui n'existent pas). Donc :

- ✅ **Comprends avant d'appliquer.** Si une étape est floue, demande « pourquoi cette
  commande ? ».
- ✅ **Applique UNE étape à la fois**, et observe le résultat.
- ✅ **Vérifie sur la doc officielle** dès que ça touche un point sensible (suppression,
  `sudo`, configuration).
- ✅ **Ça ne marche toujours pas ?** Renvoie au LLM le **nouveau** message d'erreur — on
  affine, on n'efface pas le contexte.

### À NE PAS faire

- ❌ Coller un **secret** (`.env`, token, clé).
- ❌ Exécuter une commande **sans la comprendre**, surtout avec `sudo` ou `rm`
  (une commande mal comprise peut effacer des fichiers).
- ❌ Tout changer d'un coup « au cas où ».
- ❌ Rester bloqué seul pendant des heures. Tu as cherché (méthode + doc + LLM) et tu
  sèches ? **Écris-nous** avec : ce que tu veux faire, l'erreur exacte, et ce que tu as
  déjà essayé. C'est exactement l'esprit de BIT : **tu n'es jamais seul face à la
  technique.**

---

## 5. Exemple déroulé — un vrai bug, résolu pas à pas

Mettons la méthode en pratique sur un bug **que tu vas probablement rencontrer** : juste
après avoir installé Docker (guide 6), tu testes et tu obtiens :

```
$ docker run hello-world
docker: permission denied while trying to connect to the Docker daemon socket
at unix:///var/run/docker.sock: ... connect: permission denied.
```

**1. Reproduire** — je relance `docker run hello-world` : même erreur à chaque fois.
Bug stable, parfait pour enquêter.

**2. Lire l'erreur (dernière ligne)** — le message dit `permission denied` (« permission
refusée ») pour se connecter au « Docker daemon socket ». Mot-clé : **permission**. Ce
n'est donc pas « Docker est cassé », c'est « je n'ai pas le **droit** ».

**3. Hypothèse** — « Mon utilisateur n'a pas le droit de parler à Docker. Au guide 6, on
a justement ajouté l'utilisateur au groupe `docker`… mais cette étape ne prend effet
qu'**après une reconnexion**. Je parie que je ne me suis pas reconnecté. »

**4. Tester UNE seule chose** — je vérifie d'abord l'hypothèse, sans rien casser :

```
$ groups
eleve sudo
```

Le groupe `docker` **n'apparaît pas** → mon hypothèse tient. Je teste alors la
correction (une seule action) : **redémarrer la VM** (ou `newgrp docker` pour la
session courante).

**5. Vérifier** —

```
$ groups
eleve sudo docker          ← le groupe docker est là maintenant
$ docker run hello-world
Hello from Docker!
```

Résolu. **Compris + noté** : « `permission denied` sur Docker = pas (encore) dans le
groupe `docker` → se reconnecter. »

> Et si je n'avais pas trouvé l'hypothèse ? J'aurais collé l'erreur dans un LLM avec le
> template (section 3), ou cherché `"permission denied while trying to connect to the
> Docker daemon"` sur le web → la
> [doc Docker](https://docs.docker.com/engine/install/linux-postinstall/) donne
> exactement cette solution. **Le réflexe « lire → comprendre → vérifier sur la doc »
> reste le même.**

---

> **À retenir :** débugger, ce n'est pas « connaître la réponse », c'est **savoir mener
> l'enquête**. Le message d'erreur est ton meilleur indice ; le LLM, un assistant à qui
> tu poses de **bonnes** questions ; la doc officielle, l'arbitre.

➡️ **Retour au [sommaire des guides](README.md)** · [Glossaire](08-glossaire.md)
