# Guide 2 — La virtualisation & VirtualBox

Avant d'installer Ubuntu, il faut comprendre **où** on va l'installer. On ne va pas
remplacer ton Windows : on va créer un **ordinateur virtuel** à l'intérieur de ton
ordinateur. Ça s'appelle la **virtualisation**, et l'outil qu'on utilise s'appelle
**VirtualBox**.

> ✅ **Prérequis :** la fiche [prérequis matériel](01-prerequis-materiel.md) est OK
> (surtout : **virtualisation activée** et **50 Go libres**).

---

## C'est quoi la virtualisation ?

La **virtualisation**, c'est faire tourner **un ordinateur dans un ordinateur**. Ton
PC (la machine **physique**) fait semblant d'être plusieurs ordinateurs **virtuels**,
chacun avec son propre système, isolé des autres.

```
        Ta machine physique (l'hôte)  —  Windows
   ┌─────────────────────────────────────────────────┐
   │                                                 │
   │   VirtualBox  (l'« hyperviseur »)               │
   │   ┌───────────────────────────────────────────┐ │
   │   │  Machine virtuelle (VM) — la « VM Ubuntu »│ │
   │   │  • Son propre système : Ubuntu (Linux)    │ │
   │   │  • Sa propre RAM / son propre disque      │ │
   │   │  • C'est ICI qu'on travaille              │ │
   │   └───────────────────────────────────────────┘ │
   │                                                 │
   └─────────────────────────────────────────────────┘
```

Quelques mots de vocabulaire (tu les reverras dans le [glossaire](08-glossaire.md)) :

- **Hôte (host)** : ta vraie machine — ici, ton **Windows**.
- **Invité (guest)** : le système qui tourne *dans* la fenêtre — ici, **Ubuntu**.
- **Machine virtuelle (VM)** : l'ordinateur virtuel complet (système + disque + RAM
  simulés).
- **Hyperviseur** : le logiciel qui crée et fait tourner les VM — ici, **VirtualBox**.

---

## Pourquoi on passe par une VM ? (le but)

On pourrait installer les outils directement sur Windows. On ne le fait **pas**, et
c'est volontaire :

1. **C'est isolé et réversible.** Tout vit dans la VM. Si tu casses quelque chose, tu
   supprimes la VM et tu recommences — **ton Windows n'est jamais touché**.
2. **Tu apprends le vrai environnement des pros.** La très grande majorité des serveurs
   et des outils tech tournent sous **Linux**. Travailler dans un vrai Ubuntu, c'est
   apprendre le terminal et les réflexes que tu utiliseras en entreprise.
3. **Tout le monde a le même environnement.** Quel que soit ton PC, ta VM Ubuntu est
   identique à celle des autres élèves → moins de bugs « ça marche pas chez moi », et
   on peut t'aider plus facilement.

> **Analogie :** une VM, c'est comme un **appartement témoin** monté dans un hangar.
> Tu peux y repeindre les murs, tout casser et tout refaire : le hangar (ton Windows)
> n'a pas bougé.

---

## C'est quoi VirtualBox ?

**VirtualBox** est un logiciel **gratuit** (édité par Oracle) qui crée et fait tourner
des machines virtuelles. C'est notre **hyperviseur**. On l'installe sur Windows, puis
on lui demandera de créer la VM Ubuntu au guide suivant.

> **Sur Mac à puce Apple (M1/M2/M3/M4) :** VirtualBox est instable, voire ne démarre
> pas. **Ne suis pas ce guide sur un tel Mac** — écris-nous d'abord, on te donnera la
> marche à suivre adaptée lors d'une session individuelle.

---

## Étape 1 — Télécharger VirtualBox

Va sur le site officiel : **https://www.virtualbox.org/wiki/Downloads**

Dans la section **« VirtualBox … platform packages »**, clique sur **Windows hosts**.
Un fichier `VirtualBox-….exe` se télécharge.

> ⚠️ **Télécharge uniquement depuis virtualbox.org.** Évite les sites tiers qui
> reconditionnent l'installeur (risque de logiciels indésirables).

---

## Étape 2 — Installer VirtualBox

1. Lance le fichier **`VirtualBox-….exe`** téléchargé.
2. Clique **Next** à chaque étape en **laissant les options par défaut**.
3. Un avertissement prévient que ta connexion réseau sera **brièvement coupée** pendant
   l'installation (VirtualBox installe des cartes réseau virtuelles) → clique **Yes**.
4. Accepte les éventuelles demandes d'installation de **pilotes Oracle** (« Voulez-vous
   installer ce logiciel de périphérique ? » → **Installer**).
5. Termine avec **Install** puis **Finish**. VirtualBox s'ouvre.

![Fenêtre principale de VirtualBox après installation](img/virtualbox-accueil.png)

Tu vois la fenêtre **« Oracle VirtualBox – Gestionnaire de machines »**, encore vide
(aucune VM pour l'instant). C'est normal : on crée la VM au guide suivant.

---

## Problèmes fréquents

| Symptôme | Cause | Solution |
|----------|-------|----------|
| L'installeur plante ou la VM refusera de démarrer plus tard | Virtualisation désactivée dans le BIOS | Reviens à l'[étape 4 des prérequis](01-prerequis-materiel.md#étape-4--vérifier-la-virtualisation-vt-x--amd-v) |
| `VT-x is not available` au lancement d'une VM | VT-x désactivé, ou **Hyper-V / WSL** occupe la virtualisation | Active VT-x dans le BIOS ; si besoin, on désactive Hyper-V ensemble |
| Avertissement réseau pendant l'install | Normal (cartes réseau virtuelles) | Clique **Yes** / **Continuer** |
| Sur Mac Apple Silicon, VirtualBox ne démarre pas | VirtualBox mal supporté sur puces M | **Stoppe** et écris-nous : on bascule sur la solution adaptée |

> **Toujours bloqué après ces pistes ?** Déroule la
> [méthode de débogage (guide 9)](09-debugger-et-demander-de-laide.md) — lire l'erreur,
> chercher, bien demander à un LLM — puis écris-nous si besoin. Tu n'es jamais seul.

➡️ **Suite : [Ubuntu : c'est quoi un OS, et télécharger l'ISO](03-ubuntu-os-et-iso.md)**
