import pygame
import os

class SoundManager:
    def __init__(self):
        # Initialisation de pygame mixer avec des paramètres optimisés
        try:
            pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=1024)
            pygame.mixer.init()
            self.sounds_enabled = True
            print("[AUDIO] Système audio initialisé avec succès")
        except pygame.error as e:
            print(f"[AUDIO] Impossible d'initialiser l'audio: {e}")
            self.sounds_enabled = False
            
        self.sounds = {}
        self.music_volume = 0.5
        self.sfx_volume = 0.7
        
        # Liste des sons disponibles (créer ces fichiers pour avoir du son)
        self.sound_files = {
            'click': 'sounds/click.wav',           # Son de clic sur bouton
            'place_stone': 'sounds/place.wav',    # Son de placement de pierre
            'win': 'sounds/victory.wav',          # Son de victoire
            'lose': 'sounds/defeat.wav',          # Son de défaite
            'connect': 'sounds/connect.wav',      # Son de connexion
            'error': 'sounds/error.wav',          # Son d'erreur
            'waiting': 'sounds/waiting.wav'       # Son d'attente
        }
        
        self.load_sounds()
    
    def load_sounds(self):
        """Charge les fichiers son s'ils existent"""
        if not self.sounds_enabled:
            return
            
        for name, path in self.sound_files.items():
            full_path = os.path.join(os.path.dirname(__file__), path)
            if os.path.exists(full_path):
                try:
                    self.sounds[name] = pygame.mixer.Sound(full_path)
                    self.sounds[name].set_volume(self.sfx_volume)
                    print(f"[AUDIO] Son chargé: {name}")
                except pygame.error as e:
                    print(f"[AUDIO] Erreur lors du chargement de {path}: {e}")
            else:
                print(f"[AUDIO] Fichier manquant: {full_path}")
    
    def play_sound(self, sound_name):
        """Joue un son s'il est chargé et disponible"""
        if not self.sounds_enabled:
            return
            
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
                print(f"[AUDIO] Lecture: {sound_name}")
            except pygame.error as e:
                print(f"[AUDIO] Erreur lecture {sound_name}: {e}")
        else:
            print(f"[AUDIO] Son non disponible: {sound_name}")
    
    def play_music(self, music_file):
        """Joue une musique de fond en boucle"""
        if not self.sounds_enabled:
            return
            
        full_path = os.path.join(os.path.dirname(__file__), music_file)
        if os.path.exists(full_path):
            try:
                pygame.mixer.music.load(full_path)
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(-1)  # Joue en boucle infinie
                print(f"[AUDIO] Musique lancée: {music_file}")
            except pygame.error as e:
                print(f"[AUDIO] Erreur musique {music_file}: {e}")
        else:
            print(f"[AUDIO] Fichier musique manquant: {full_path}")
    
    def stop_music(self):
        """Arrête la musique de fond"""
        if self.sounds_enabled:
            pygame.mixer.music.stop()
            print("[AUDIO] Musique arrêtée")
    
    def set_sfx_volume(self, volume):
        """Règle le volume des effets sonores (0.0 à 1.0)"""
        self.sfx_volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.sfx_volume)
        print(f"[AUDIO] Volume des effets: {self.sfx_volume:.1f}")
    
    def set_music_volume(self, volume):
        """Règle le volume de la musique (0.0 à 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.sounds_enabled:
            pygame.mixer.music.set_volume(self.music_volume)
        print(f"[AUDIO] Volume de la musique: {self.music_volume:.1f}")
    
    def toggle_sounds(self):
        """Active/désactive les sons"""
        self.sounds_enabled = not self.sounds_enabled
        print(f"[AUDIO] Sons {'activés' if self.sounds_enabled else 'désactivés'}")
        return self.sounds_enabled

# Instance globale du gestionnaire de sons
sound_manager = SoundManager()