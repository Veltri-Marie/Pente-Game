# Informations sur les fichiers audio pour le jeu Pente

## Fichiers audio requis (optionnels)

Pour une experience complete avec du son, placez ces fichiers dans le dossier sounds/:

### Effets sonores (.wav recommandé)
- **click.wav** : Son de clic sur les boutons
- **place.wav** : Son de placement d'une pierre sur le plateau  
- **victory.wav** : Son de victoire
- **defeat.wav** : Son de défaite
- **connect.wav** : Son de connexion au serveur
- **error.wav** : Son d'erreur
- **waiting.wav** : Son d'attente

### Musique de fond (.mp3 ou .ogg)
- **background.mp3** : Musique d'ambiance (optionnelle)

## Generation de sons de test

Vous pouvez utiliser des outils en ligne ou des logiciels comme Audacity pour créer ces sons.

Pour des tests rapides, le jeu fonctionne parfaitement sans audio.
Les messages d'information audio apparaîtront dans la console.

## État actuel
- Le système audio est configuré et prêt
- Les sons sont chargés automatiquement s'ils existent
- Aucun son n'est requis pour jouer
- Volume réglable dans le code (sounds.py)