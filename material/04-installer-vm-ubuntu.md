# Guide 4 — Créer & installer la VM Ubuntu (pas à pas)

Tu as **VirtualBox** installé ([guide 2](02-virtualisation-virtualbox.md)) et l'**ISO
d'Ubuntu** téléchargée ([guide 3](03-ubuntu-os-et-iso.md)). On va maintenant **créer la
machine virtuelle** puis **installer Ubuntu dedans**. Compte ~30–45 minutes (surtout de
l'attente).

> **Rappel rassurant :** tout se passe **dans la VM**. Même quand l'installeur parlera
> d'« effacer le disque », il s'agit du **disque virtuel** de la VM — **ton Windows et
> tes fichiers ne sont jamais touchés.**

---

## Partie A — Créer la machine virtuelle

### Étape 1 — Nouvelle VM

Dans VirtualBox, clique sur **« Nouvelle »** (Machine → Nouvelle).

1. **Nom** : `BIT-Ubuntu` (ou ce que tu veux).
2. **Dossier** : laisse par défaut.
3. **Image ISO** : clique sur le menu déroulant → **Autre…** → sélectionne ton fichier
   `ubuntu-24.04-desktop-amd64.iso`.
4. **Coche** la case **« Skip Unattended Installation »** (Ignorer l'installation
   automatique). On veut faire l'installation **nous-mêmes**, c'est plus pédagogique.

![Assistant Nouvelle VM avec l'ISO Ubuntu sélectionnée](img/vbox-new-vm.png)

> VirtualBox reconnaît qu'il s'agit d'Ubuntu et règle le **type/version** tout seul.

### Étape 2 — Mémoire & processeurs

- **Mémoire vive (RAM)** : règle le curseur sur **4096 Mo** (4 Go). Si ton PC a 16 Go,
  tu peux monter à **8192 Mo** (8 Go).
  > ⚠️ **Ne dépasse jamais ~la moitié de ta RAM physique** (zone verte du curseur),
  > sinon ton Windows devient lent.
- **Processeurs** : règle sur **2 CPU** (reste dans la zone verte).

### Étape 3 — Disque dur virtuel

1. Choisis **« Créer un disque dur virtuel maintenant »**.
2. Taille : **40 Go** (minimum confortable ; 50 Go si tu as la place).
3. Laisse le type par défaut (**VDI**, **alloué dynamiquement**) → le fichier ne
   grossit que **au fur et à mesure**, il ne prend pas 40 Go d'un coup.

Clique **Terminer**. Ta VM apparaît dans la liste, **éteinte**.

---

## Partie B — Installer Ubuntu dans la VM

### Étape 4 — Démarrer la VM

Sélectionne ta VM `BIT-Ubuntu` → clique **« Démarrer »** (la flèche verte). Une fenêtre
s'ouvre : c'est l'écran de ta machine virtuelle. Elle **démarre sur l'ISO** d'Ubuntu.

> **Souris « capturée » ?** Si la VM capture ta souris/clavier, la touche pour les
> **libérer** est affichée en bas à droite (par défaut **`Ctrl droit`**).

### Étape 5 — Lancer l'installation

1. Au menu de démarrage, laisse **« Try or Install Ubuntu »** (touche `Entrée`).
2. Après quelques instants, choisis la **langue** (Français) → **Installer Ubuntu**.
3. **Disposition du clavier** : choisis **Français** → teste dans la case → **Suivant**.
4. **Connexion** : laisse les options par défaut.

### Étape 6 — Type d'installation

1. Choisis l'installation **« Normale »** (ou « Interactive »).
2. Tu peux **décocher** « Télécharger les mises à jour pendant l'installation » pour
   aller plus vite (tu les feras après).
3. À l'étape du disque, choisis **« Effacer le disque et installer Ubuntu »**.

> **C'est SANS DANGER** : ce « disque » est le **disque virtuel de 40 Go** que tu
> viens de créer, **vide**. Ça **n'efface pas** ton Windows ni tes fichiers — ils sont
> sur la machine hôte, hors de la VM.

### Étape 7 — Ton compte

1. **Ton nom**.
2. **Nom de l'ordinateur** (ex : `bit-ubuntu`).
3. **Nom d'utilisateur** (ex : `eleve`) — retiens-le.
4. **Mot de passe** — ⚠️ **note-le précieusement** : tu le retaperas souvent dans le
   terminal (commandes `sudo`).
5. Coche éventuellement **« Se connecter automatiquement »** pour ne pas le retaper à
   chaque démarrage de la VM.

### Étape 8 — Laisser installer, puis redémarrer

L'installation se lance (**10–20 min**, c'est le moment d'une pause).

À la fin, un message propose de **redémarrer**. Clique **« Redémarrer maintenant »**.

> **Si la VM redemande « Please remove the installation medium »** : Ubuntu te
> demande d'« enlever le DVD ». Reviens dans VirtualBox → menu **Périphériques →
> Lecteurs optiques → Retirer le disque du lecteur** si besoin, puis appuie sur
> `Entrée`. (En général VirtualBox éjecte l'ISO automatiquement.)

### Étape 9 — Premier démarrage d'Ubuntu

La VM redémarre **sur Ubuntu installé**. Connecte-toi avec ton mot de passe. Tu arrives
sur le **bureau Ubuntu** : tu as une vraie machine Linux qui tourne dans une fenêtre !

![Bureau Ubuntu fraîchement installé dans VirtualBox](img/ubuntu-bureau.png)

Ouvre le **Terminal** d'Ubuntu (icône dans les applications, ou `Ctrl + Alt + T`) : c'est
**là** que se passeront tous les guides suivants.

---

## (Recommandé) Étape 10 — Mettre Ubuntu à jour

Dans le terminal Ubuntu, tape (il demandera ton mot de passe) :

```bash
sudo apt update && sudo apt upgrade -y
```

- `sudo` → « exécuter en administrateur » (d'où le mot de passe).
- `apt update` → rafraîchit la liste des logiciels disponibles.
- `apt upgrade -y` → installe les mises à jour (`-y` = « oui à tout »).

---

## Problèmes fréquents

| Symptôme | Cause | Solution |
|----------|-------|----------|
| `VT-x is not available` au démarrage de la VM | Virtualisation désactivée / Hyper-V en conflit | Voir [prérequis étape 4](01-prerequis-materiel.md#étape-4--vérifier-la-virtualisation-vt-x--amd-v) ; on désactive Hyper-V ensemble si besoin |
| La VM est minuscule / ne se redimensionne pas | « Guest Additions » pas encore installées | Menu **Périphériques → Insérer l'image CD des Additions invité** (optionnel, on peut le faire ensemble) |
| La souris reste « bloquée » dans la VM | Souris capturée | Appuie sur **`Ctrl droit`** pour la libérer |
| Boucle de redémarrage sur l'installeur | L'ISO est restée « insérée » | **Périphériques → Lecteurs optiques → Retirer le disque**, puis redémarre |
| Installation très lente | Peu de RAM/CPU alloués ou disque HDD | Vérifie 4 Go RAM + 2 CPU ; patiente sur HDD |

> **Toujours bloqué après ces pistes ?** Déroule la
> [méthode de débogage (guide 9)](09-debugger-et-demander-de-laide.md) — lire l'erreur,
> chercher, bien demander à un LLM — puis écris-nous si besoin. Tu n'es jamais seul.

➡️ **Suite : [GitHub : compte + cloner le repo (dans Ubuntu)](05-github-compte-et-clone.md)**
