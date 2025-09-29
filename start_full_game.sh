#!/bin/bash

echo "*** LANCEMENT COMPLET - PENTE AVEC 2 JOUEURS ***"
echo "================================================"

# Aller dans le dossier du projet
cd "$(dirname "$0")"

# Fonction pour nettoyer les processus en cas d'interruption
cleanup() {
    echo ""
    echo "*** Arret du jeu en cours ***"
    
    # Arrêter le serveur
    if [ ! -z "$SERVER_PID" ]; then
        kill $SERVER_PID 2>/dev/null
        echo "- Serveur arrete"
    fi
    
    # Arrêter les clients
    if [ ! -z "$CLIENT1_PID" ]; then
        kill $CLIENT1_PID 2>/dev/null
        echo "- Client 1 arrete"
    fi
    
    if [ ! -z "$CLIENT2_PID" ]; then
        kill $CLIENT2_PID 2>/dev/null
        echo "- Client 2 arrete"
    fi
    
    echo "*** Jeu arrete proprement ***"
    exit 0
}

# Capturer Ctrl+C pour nettoyer
trap cleanup INT TERM

echo "1. Verification de la compilation du serveur..."
if [ ! -f "Server/build/Server" ]; then
    echo "   Compilation du serveur en cours..."
    cd Server
    mkdir -p build
    cd build
    cmake .. && make
    chmod +x Server
    cd ../..
    
    if [ ! -f "Server/build/Server" ]; then
        echo "ERREUR: Impossible de compiler le serveur."
        exit 1
    fi
    echo "   ✓ Serveur compile avec succes"
else
    echo "   ✓ Serveur deja compile"
fi

echo ""
echo "2. Verification de l'environnement Python..."
if [ ! -d ".venv" ]; then
    echo "   Configuration de l'environnement Python..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pygame pygame-gui
    echo "   ✓ Environnement Python configure"
else
    echo "   ✓ Environnement Python deja configure"
fi

echo ""
echo "3. Demarrage du serveur..."
cd Server/build
./Server &
SERVER_PID=$!
cd ../..
sleep 2
echo "   ✓ Serveur demarre (PID: $SERVER_PID)"

echo ""
echo "4. Demarrage du Client 1 (Joueur 1)..."
cd Client
../.venv/bin/python main.py &
CLIENT1_PID=$!
cd ..
sleep 1
echo "   ✓ Client 1 demarre (PID: $CLIENT1_PID)"

echo ""
echo "5. Demarrage du Client 2 (Joueur 2)..."
cd Client
../.venv/bin/python main.py &
CLIENT2_PID=$!
cd ..
sleep 1
echo "   ✓ Client 2 demarre (PID: $CLIENT2_PID)"

echo ""
echo "*** JEU PRETE A JOUER ***"
echo "========================"
echo ""
echo "INSTRUCTIONS:"
echo "1. Connectez-vous sur les 2 clients avec des noms differents"
echo "   Exemple: Joueur1 / mot de passe: ok"
echo "           Joueur2 / mot de passe: ok"
echo ""
echo "2. Sur le Client 1: Cliquez '[+] Creer une partie'"
echo "3. Sur le Client 2: Cliquez sur la partie creee pour la rejoindre"
echo "4. Jouez ! Premier a aligner 5 pierres gagne"
echo ""
echo "Appuyez sur Ctrl+C pour arreter tout le jeu"
echo ""

# Attendre que l'utilisateur arrête avec Ctrl+C ou qu'un processus se termine
while kill -0 $SERVER_PID 2>/dev/null && kill -0 $CLIENT1_PID 2>/dev/null && kill -0 $CLIENT2_PID 2>/dev/null; do
    sleep 1
done

echo "Un processus s'est arrete. Nettoyage..."
cleanup