# Guide 1 — Ton ordinateur est-il prêt ? (prérequis matériel)

Pendant le parcours, tu vas installer un petit **environnement technique** sur ta
machine : **VirtualBox**, une machine **Ubuntu** (Linux) et **Docker** dedans.
Bonne nouvelle : **tout reste isolé et réversible** — ton Windows n'est pas modifié,
et tu peux tout supprimer à la fin sans laisser de trace.

Avant de commencer, vérifie en **5 minutes** que ton matériel va suivre. Pas besoin
d'un ordinateur récent ou puissant : il faut surtout vérifier **4 points simples**.

> 💡 La case la plus souvent oubliée n'est **pas** la puissance — c'est l'**espace
> disque libre**. C'est le point n°1 qui bloque les débutants.

---

## ✅ Check-list — à cocher avant de te lancer

- [ ] **Mémoire (RAM) : au moins 8 Go** — 8 Go suffisent, 16 Go = très confortable.
- [ ] **Processeur 64 bits, au moins 2 cœurs** — quasi tous les PC des 8 dernières
      années conviennent.
- [ ] **Espace disque LIBRE : au moins 50 Go** — ⚠️ ce n'est pas la *taille* du
      disque, mais la place **encore libre**.
- [ ] **La virtualisation (VT-x / AMD-V) est activée** — sans elle, VirtualBox
      refuse de démarrer.
- [ ] **Système : Windows 10/11, macOS ou Linux (64 bits)** + une connexion internet
      stable.

**Les 4 premières cases cochées ? Tu es prêt(e).** Une case incertaine ? Pas de
panique : la section « Comment vérifier » ci-dessous te montre exactement où cliquer,
et on t'accompagne individuellement si besoin. **Personne ne reste seul face à un
blocage technique — c'est l'esprit de BIT.**

---

## Les seuils en détail

| Critère | Minimum (ça marche) | Recommandé (confort) | Pourquoi ça compte |
|---------|---------------------|----------------------|--------------------|
| **Mémoire RAM** | 8 Go | 16 Go | La VM partage la mémoire avec ton Windows. Sous 8 Go, tout devient lent. |
| **Processeur** | 2 cœurs / 64 bits | 4 cœurs / 8 threads | Suffisant pour les exercices. Aucune carte graphique dédiée nécessaire. |
| **Disque LIBRE** | 50 Go libres | 80 Go libres | L'installation occupe ~30–40 Go. Windows devient instable sous 10 Go libres. |
| **Type de disque** | HDD (lent) | SSD | Sur SSD tout démarre vite. Sur vieux HDD c'est lent, mais ça marche. |
| **Virtualisation** | VT-x / AMD-V activée | idem | **Obligatoire.** Souvent désactivée par défaut → voir l'étape 4. |

> 🔑 **Règle d'or :** le confort dépend bien plus du **SSD** et de l'**espace libre**
> que de la puissance brute du processeur. Un PC modeste avec un SSD et 50 Go libres
> vivra mieux le parcours qu'un PC puissant au disque saturé.

---

## Comment vérifier (Windows 10 / 11)

> 🍎 **Sur Mac :** menu  → *À propos de ce Mac* pour la RAM, le processeur et le
> stockage. ⚠️ **Important** : sur les Mac à puce Apple (M1/M2/M3/M4), VirtualBox
> fonctionne mal voire pas du tout. **Si tu es sur un Mac récent, écris-nous avant
> de commencer** : on te donnera la marche à suivre adaptée (session individuelle).

### Étape 1 — Voir ta RAM

Touche **`Windows + Pause`**. Ou : clic droit sur le menu Démarrer → **Système**.
Lis la ligne **« Mémoire RAM installée »**.

### Étape 2 — Voir ton processeur

Même écran que l'étape 1 : lignes **« Processeur »** et **« Type du système »**
(doit indiquer **64 bits**).

### Étape 3 — Voir l'espace disque LIBRE

Ouvre l'**Explorateur de fichiers** → **Ce PC**. Sous le disque **(C:)**, lis
« … **Go libres** sur … Go ». **C'est le premier chiffre qui compte.**

> 🧹 **Manque de place ?** Vide la corbeille, désinstalle les logiciels inutilisés,
> ou déplace photos/vidéos sur un disque externe ou un cloud. **Objectif : 50 Go
> libres minimum.**

### Étape 4 — Vérifier la virtualisation (VT-x / AMD-V)

`Ctrl + Maj + Échap` → onglet **Performance** → **Processeur**. En bas à droite,
cherche **« Virtualisation »** : doit indiquer **« Activé »**.

- ✅ **« Activé »** → parfait, tu peux continuer.
- ❌ **« Désactivé »** → il faut l'activer dans le **BIOS** au démarrage (touche
  `F2`, `F10` ou `Suppr` selon la marque), rubrique **« Intel VT-x »**, **« SVM
  Mode »** ou **« Virtualization »**.
  > ⚠️ **Ne le fais pas seul si tu n'es pas à l'aise** — on le fait **ensemble** lors
  > d'une session dédiée en début de parcours.

---

## Cas concret — lire une fiche système

Exemple d'un vrai PC testé : **i7-1165G7 · 16 Go RAM · disque 466 Go utilisés sur 477**.

- ✅ **RAM & processeur : excellents.** 16 Go et un i7 récent = très confortable.
- ❌ **Disque : bloquant en l'état.** Seulement **~11 Go libres** alors qu'il en faut
  50. Ce PC ne planterait pas par manque de puissance, mais par **disque plein**.
  **Action avant le parcours : libérer 40–50 Go.**

C'est l'illustration parfaite de la règle d'or : **on regarde la place libre, pas la
taille du disque ni la puissance.**

---

> Un doute, une case non cochée, un mot inconnu ? C'est **normal et prévu**. Envoie-nous
> une capture d'écran de ton écran **« Système »** — on regarde ensemble. Vérifier son
> matériel fait **déjà partie du parcours** : tu n'es jamais seul(e) face à la technique.

➡️ **Suite : [La virtualisation & VirtualBox](02-virtualisation-virtualbox.md)**
