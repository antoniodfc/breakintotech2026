# Guide 3 — Ubuntu : c'est quoi un OS, et télécharger l'ISO

VirtualBox est prêt ([guide précédent](02-virtualisation-virtualbox.md)). Il nous faut
maintenant **un système à installer dedans** : ce sera **Ubuntu**. Avant de le
télécharger, comprenons ce qu'on installe.

---

## C'est quoi un « système d'exploitation » (OS) ?

Un **système d'exploitation** (en anglais **OS**, *Operating System*) est le **logiciel
principal** d'un ordinateur : celui qui démarre en premier et qui fait le lien entre le
**matériel** (écran, clavier, disque, mémoire) et **tes applications**.

Sans OS, un ordinateur est une boîte inerte. C'est l'OS qui :

- affiche le bureau, les fenêtres, les dossiers ;
- lance et gère tes programmes ;
- gère les fichiers, le réseau, les utilisateurs.

Tu en utilises déjà un : **Windows** est un OS. **macOS** en est un autre. **Linux**
en est un troisième — et c'est celui qu'on va utiliser.

```
        Tes applications  (navigateur, terminal, Docker…)
                       ▲
                       │  l'OS fait le lien
                       ▼
        Système d'exploitation  (Windows / macOS / Linux)
                       ▲
                       │
                       ▼
        Le matériel  (processeur, mémoire, disque, écran)
```

---

## Linux, Ubuntu, « distribution » : on démêle

- **Linux** est le **cœur** (le « noyau ») d'un système libre et gratuit, né en 1991.
  Il fait tourner l'immense majorité des **serveurs**, des **smartphones Android**, des
  box internet, etc.
- Autour de ce noyau, des équipes assemblent un système complet (bureau, outils,
  logithèque) : ça s'appelle une **distribution** Linux.
- **Ubuntu** est **la distribution Linux la plus populaire pour débuter** : simple,
  bien finie, énorme communauté.

> **Analogie :** Linux est le **moteur**. Une *distribution* (Ubuntu, Debian,
> Fedora…) est la **voiture complète** construite autour de ce moteur. On choisit
> Ubuntu parce que c'est la voiture la plus facile à conduire quand on débute.

---

## Pourquoi Ubuntu (et pas Windows) pour le parcours ?

1. **C'est l'environnement des pros.** Serveurs, cloud, Docker, DevOps… tournent
   massivement sous Linux. Apprendre Ubuntu, c'est apprendre les **vrais** outils du
   métier.
2. **Le terminal y est roi.** Sous Linux, on pilote la machine en **ligne de commande**
   — la compétence de base que tu développes tout au long du parcours.
3. **C'est gratuit et libre.** Aucune licence à payer, tout est ouvert.
4. **Tout le monde a le même système.** La VM Ubuntu est identique pour tous les
   élèves → on diagnostique et on s'entraide bien plus facilement.

---

## C'est quoi un « fichier ISO » ?

Pour installer Ubuntu, on télécharge un **fichier ISO**. Une **ISO** est l'**image
complète d'un disque d'installation** dans un seul fichier (`.iso`) — l'équivalent
numérique d'un **DVD d'installation**.

On donnera ce fichier ISO à VirtualBox (guide suivant), comme si on **insérait le DVD**
dans la VM pour lancer l'installation d'Ubuntu.

---

## Étape 1 — Télécharger l'ISO d'Ubuntu

1. Va sur le site officiel : **https://ubuntu.com/download/desktop**
2. Télécharge la dernière version **LTS** proposée (ex : *Ubuntu 24.04 LTS*).

   > **LTS** = *Long Term Support* (« support longue durée ») : une version stable,
   > maintenue **5 ans**. C'est celle à privilégier — pas les versions intermédiaires.

3. Le téléchargement est **lourd (~5–6 Go)** : lance-le sur une connexion stable et
   sois patient. Tu obtiens un fichier du type `ubuntu-24.04-desktop-amd64.iso`.

![Page de téléchargement d'Ubuntu Desktop LTS](img/ubuntu-download.png)

> **`amd64`** = la version pour processeurs **64 bits** classiques (Intel/AMD) —
> celle qu'il te faut sur un PC Windows. (Rien à voir avec la marque AMD.)

---

## Étape 2 — Repérer le fichier téléchargé

Note **où** l'ISO a été enregistrée (en général le dossier **Téléchargements**). Tu en
auras besoin au guide suivant pour l'indiquer à VirtualBox.

> ✅ **Tu n'as rien à ouvrir ni à graver.** L'ISO reste un simple fichier ; c'est
> VirtualBox qui s'en servira.

---

## Problèmes fréquents

| Symptôme | Cause | Solution |
|----------|-------|----------|
| Téléchargement très long / qui coupe | Fichier lourd (~5–6 Go) + connexion instable | Relance sur une connexion stable ; évite le Wi-Fi faible |
| Tu ne retrouves pas l'ISO | Rangée dans **Téléchargements** par défaut | Ouvre l'Explorateur → **Téléchargements**, cherche `ubuntu-…-amd64.iso` |
| Doute sur la version à prendre | Plusieurs versions affichées | Prends toujours la **LTS** la plus récente (ex : 24.04 LTS) |

> **Toujours bloqué après ces pistes ?** Déroule la
> [méthode de débogage (guide 9)](09-debugger-et-demander-de-laide.md) — lire l'erreur,
> chercher, bien demander à un LLM — puis écris-nous si besoin. Tu n'es jamais seul.

➡️ **Suite : [Créer & installer la VM Ubuntu (pas à pas)](04-installer-vm-ubuntu.md)**
