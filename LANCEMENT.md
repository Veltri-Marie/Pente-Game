# *** GUIDE COMPLET - JEU PENTE ***

## PRESENTATION
Jeu de Pente multijoueur en temps réel avec serveur C et client Python.
But: Aligner 5 pierres consécutivement pour gagner.

## ARCHITECTURE
- **Serveur**: C avec SQLite (gestion parties et utilisateurs)
- **Client**: Python avec Pygame (interface graphique moderne)
- **Réseau**: Communication par sockets binaires
- **Audio**: Support sons d'ambiance (optionnel)

## INSTALLATION RAPIDE

### 1. Compilation du serveur
```bash
cd Server
mkdir -p build && cd build
cmake .. && make
chmod +x Server
```

### 2. Installation client Python
```bash
# Environnement virtuel déjà configuré dans .venv/
# Dépendances: pygame, pygame-gui (déjà installées)
```

## LANCEMENT

### Option A: Scripts automatiques (RECOMMANDE)
```bash
# Terminal 1 - Serveur
./start_server.sh

# Terminal 2 - Client  
./start_client.sh
```

### Option B: Lancement manuel
```bash
# Serveur
cd Server/build && ./Server

# Client
cd Client && ../.venv/bin/python main.py
```

### Option C: Lancement complet
```bash
# Démarre serveur + client automatiquement
./start_game.sh
```

## CONFIGURATION

### Réseau
- **Port**: 55556 (modifiable dans config.py et config.h)
- **Adresse**: 127.0.0.1 (localhost)
- **Connexions**: Maximum 10 clients simultanés

### Audio (Optionnel)
- Placez les fichiers .wav dans `Client/sounds/`
- Voir `Client/sounds/README_AUDIO.md` pour la liste
- Le jeu fonctionne parfaitement sans audio

## FONCTIONNALITES

### Interface Moderne
- Design dégradé bleu/doré sans émojis
- Animations de particules scintillantes  
- Plateau 3D avec texture bois réaliste
- Pions avec effets d'ombres et reflets
- Interface entièrement en français

### Gameplay
- Connexion avec nom d'utilisateur/mot de passe
- Création et rejointe de parties
- Jeu en temps réel avec synchronisation
- Système de scores et statistiques
- Abandon de partie possible

### Technique
- 60 FPS fluides avec animations
- Compatible tous systèmes (pas d'émojis)
- Gestion d'erreurs robuste
- Code modulaire et documenté

## RESOLUTION DE PROBLEMES

### Serveur ne démarre pas
- Vérifiez que le port 55556 est libre
- Recompilez avec `make clean && make`
- Vérifiez les permissions: `chmod +x Server`

### Client ne se connecte pas  
- Assurez-vous que le serveur est démarré
- Vérifiez l'adresse/port dans config.py
- Testez avec: `telnet 127.0.0.1 55556`

### Problèmes audio
- Audio optionnel, ignorez les messages [AUDIO]
- Vérifiez pygame: `python -c "import pygame; print('OK')"`
- Placez des fichiers .wav dans Client/sounds/

### Erreurs de compilation
- Installez cmake: `brew install cmake` (macOS)
- Vérifiez GCC/Clang disponible
- Supprimez build/ et recommencez

## STRUCTURE DU PROJET

```
Pente_Game_Code/
├── Server/                 # Serveur C
│   ├── *.c, *.h           # Code source
│   ├── CMakeLists.txt     # Configuration build
│   └── build/Server       # Exécutable compilé
├── Client/                # Client Python  
│   ├── *.py              # Code source
│   ├── theme.json        # Thème interface
│   └── sounds/           # Fichiers audio (optionnel)
├── .venv/                # Environnement Python
├── start_*.sh           # Scripts de lancement
└── LANCEMENT.md         # Ce guide
```

## COMMANDES DE JEU

### Dans l'interface
- **Connexion**: Entrez nom/mot de passe puis "Se connecter"
- **Lobby**: "[+] Créer une partie" ou cliquez sur une partie existante
- **Jeu**: Cliquez sur une intersection pour placer votre pierre
- **Abandon**: Bouton "Abandonner" pendant la partie

### Objectif
- Alignez 5 pierres consécutivement (horizontal/vertical/diagonal)
- Premier à aligner gagne la partie
- Score augmente avec les victoires

## SUPPORT

Le jeu est maintenant entièrement fonctionnel avec:
- ✓ Interface moderne et compatible
- ✓ Serveur multi-clients robuste  
- ✓ Réseau optimisé et stable
- ✓ Audio préparé (optionnel)
- ✓ Code propre et documenté

Bon jeu ! ***