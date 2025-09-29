import pygame
import pygame_gui
import math
from config import *
from sounds import sound_manager

class GUIManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        
        # Fond dégradé moderne
        self.background = self.create_gradient_background()
        
        self.state_manager = INITIAL_STATE
        self.manager = pygame_gui.UIManager(SCREEN_SIZE, "theme.json")
        
        # Variables pour l'animation
        self.animation_time = 0
        self.particles = []

    def create_gradient_background(self):
        """Crée un fond avec dégradé moderne"""
        background = pygame.Surface(SCREEN_SIZE)
        
        # Dégradé du haut vers le bas : bleu foncé vers noir
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            # Couleur qui va du bleu foncé (0x1a1a2e) vers le noir
            r = int(26 * (1 - ratio))
            g = int(26 * (1 - ratio)) 
            b = int(46 * (1 - ratio))
            color = (r, g, b)
            pygame.draw.line(background, color, (0, y), (SCREEN_WIDTH, y))
            
        return background

    def draw_animated_background(self):
        """Dessine un fond animé avec des particules"""
        self.screen.blit(self.background, (0, 0))
        
        # Animation des particules en arrière-plan
        self.animation_time += 0.02
        for i in range(20):
            x = (50 + i * 50 + math.sin(self.animation_time + i) * 30) % SCREEN_WIDTH
            y = (50 + i * 35 + math.cos(self.animation_time * 0.7 + i) * 20) % SCREEN_HEIGHT
            alpha = int(100 + 50 * math.sin(self.animation_time + i))
            
            # Particules dorées scintillantes
            particle_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
            particle_surface.fill((255, 215, 0, alpha))
            self.screen.blit(particle_surface, (x, y))

    @staticmethod
    def display_new_game_error(create_btn, logout_btn, new_game_failed_lbl, confirm_new_game_failed_btn):
        create_btn.set_text("")
        logout_btn.set_text("")
        create_btn.set_dimensions((0, 0))
        logout_btn.set_dimensions((0, 0))
        new_game_failed_lbl.set_text("ERREUR - Impossible de creer une partie maintenant")
        confirm_new_game_failed_btn.set_dimensions((200, 50))
        confirm_new_game_failed_btn.set_position((412, 450))
        confirm_new_game_failed_btn.set_text("Compris")

    def show_authentication(self):
        pygame.display.set_caption("PENTE - Connexion")
        self.manager.clear_and_reset()
        
        # Son de connexion
        sound_manager.play_sound('connect')

        # Titre principal
        title_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 150), (400, 80)),
            text="*** PENTE ***",
            manager=self.manager,
            object_id="#main_title"
        )

        subtitle_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 220), (400, 40)),
            text="Alignez 5 pierres pour gagner !",
            manager=self.manager,
            object_id="#subtitle"
        )

        # Panneau de connexion avec style moderne
        panel_rect = pygame.Rect(280, 300, 464, 280)
        panel_surface = pygame.Surface((464, 280), pygame.SRCALPHA)
        panel_surface.fill((0, 0, 0, 180))  # Fond semi-transparent
        pygame.draw.rect(panel_surface, (65, 105, 225, 100), (0, 0, 464, 280), border_radius=15)
        pygame.draw.rect(panel_surface, (255, 215, 0), (0, 0, 464, 280), width=3, border_radius=15)

        username_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((320, 340), (140, 30)),
            text="Nom d'utilisateur:",
            manager=self.manager,
            object_id="#lbl"
        )

        pw_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((320, 400), (140, 30)),
            text="Mot de passe:",
            manager=self.manager,
            object_id="#lbl"
        )

        username_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((480, 340), (220, 35)),
            manager=self.manager,
            object_id="#text_entry"
        )

        pw_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((480, 400), (220, 35)),
            manager=self.manager,
            object_id="#text_entry"
        )
        pw_input.set_text_hidden(True)

        login_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((450, 460), (140, 50)),
            text=">> Se connecter",
            manager=self.manager,
            object_id="#login_btn"
        )

        auth_failed_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((300, 530), (424, 30)),
            text="",
            manager=self.manager,
            object_id="#error_label"
        )

        return username_lbl, pw_lbl, username_input, pw_input, login_btn, auth_failed_lbl

    def show_lobby(self, show_no_game_label=False):
        pygame.display.set_caption("PENTE - Lobby")
        self.manager.clear_and_reset()

        # Titre du lobby
        lobby_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 50), (400, 60)),
            text="*** LOBBY ***",
            manager=self.manager,
            object_id="#main_title"
        )

        # Sous-titre
        lobby_subtitle = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 110), (400, 30)),
            text="Choisissez ou creez une partie",
            manager=self.manager,
            object_id="#subtitle"
        )

        # Boutons avec icônes et style moderne
        create_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((180, 650), (240, 60)),
            text="[+] Creer une partie",
            manager=self.manager,
            object_id="#primary_btn"
        )

        logout_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((600, 650), (180, 60)),
            text="<< Deconnexion",
            manager=self.manager,
            object_id="#secondary_btn"
        )

        new_game_failed_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 350), (400, 100)),
            text="",
            manager=self.manager,
            object_id="#error_label"
        )

        confirm_new_game_failed_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((462, 480), (0, 0)),
            text="",
            manager=self.manager,
            object_id="#secondary_btn"
        )

        no_game_label = None
        if show_no_game_label:
            no_game_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((312, 300), (400, 80)),
                text="Aucune partie disponible\nCreez-en une nouvelle !",
                manager=self.manager,
                object_id="#message_label"
            )

        pygame.display.flip()
        return create_btn, logout_btn, new_game_failed_lbl, confirm_new_game_failed_btn, no_game_label

    def show_game_list(self, games, game_buttons):
        for button in game_buttons:
            button.kill()

        button_to_game_id = {}
        buttons = []
        
        # En-tête de la liste
        header_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((30, 150), (964, 40)),
            text="*** Parties disponibles - Cliquez pour rejoindre ***",
            manager=self.manager,
            object_id="#status_label"
        )

        for i, game in enumerate(games):
            # Informations du joueur avec symboles et style
            wins_symbol = "[*]" if game['wins'] > game['losses'] else "[.]"
            score_symbol = "+++" if game['score'] > 1000 else "+"
            
            game_info = (f"[{game['id']}] Partie {game['id']} | Joueur: {game['username']} | "
                        f"{score_symbol} Score: {game['score']} | "
                        f"{wins_symbol} V: {game['wins']} | X D: {game['losses']}")

            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((30, 200 + i * 70), (964, 60)),
                text=game_info,
                manager=self.manager,
                object_id="#game_btn"
            )

            button_to_game_id[button] = game['id']
            buttons.append(button)

        return buttons, button_to_game_id

    def show_inactive_game(self):
        pygame.display.set_caption("PENTE - En attente")
        self.manager.clear_and_reset()

        # Animation de points de suspension
        dots = "." * (int(self.animation_time * 2) % 4)
        
        # Titre avec animation
        waiting_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 250), (400, 80)),
            text="*** EN ATTENTE ***",
            manager=self.manager,
            object_id="#main_title"
        )

        pending_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((212, 350), (600, 60)),
            text=f"Recherche d'un adversaire{dots}\nPreparez votre strategie !",
            manager=self.manager,
            object_id="#pending_label"
        )

        lobby_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((412, 480), (200, 60)),
            text="<< Retour au lobby",
            manager=self.manager,
            object_id="#secondary_btn"
        )

        error_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((312, 570), (400, 40)),
            text="",
            manager=self.manager,
            object_id="#error_label"
        )

        pygame.display.update()
        return pending_lbl, lobby_btn, error_lbl

    def show_board(self, board_state, cell_size=30, status_message="A votre tour !"):
        pygame.display.set_caption("PENTE - Partie en cours")
        self.manager.clear_and_reset()

        # Fond dégradé pour le jeu
        game_background = pygame.Surface(SCREEN_SIZE)
        
        # Dégradé plus sombre pour le jeu
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(15 * (1 - ratio))
            g = int(20 * (1 - ratio))
            b = int(35 * (1 - ratio))
            color = (r, g, b)
            pygame.draw.line(game_background, color, (0, y), (SCREEN_WIDTH, y))
        
        self.background = game_background

        # Calcul pour centrer le plateau
        grid_width = 19 * cell_size
        grid_height = 19 * cell_size
        grid_offset_x = (SCREEN_WIDTH - grid_width) // 2
        grid_offset_y = (SCREEN_HEIGHT - grid_height) // 2 + 20

        # Fond du plateau avec effet de bois luxueux
        board_background = pygame.Rect(grid_offset_x - 20, grid_offset_y - 20, 
                                     grid_width + 40, grid_height + 40)
        
        # Ombre portée
        shadow_rect = pygame.Rect(board_background.x + 5, board_background.y + 5,
                                board_background.width, board_background.height)
        pygame.draw.rect(self.background, (0, 0, 0, 100), shadow_rect, border_radius=15)
        
        # Fond du plateau
        pygame.draw.rect(self.background, (139, 120, 93), board_background, border_radius=15)
        pygame.draw.rect(self.background, (205, 133, 63), board_background, width=3, border_radius=15)

        # Plateau de jeu avec texture
        board_rect = pygame.Rect(grid_offset_x, grid_offset_y, grid_width, grid_height)
        pygame.draw.rect(self.background, (218, 165, 32), board_rect)

        # Dessiner la grille avec style
        for x in range(20):  # 20 lignes pour 19 cases
            start_pos = (grid_offset_x + x * cell_size, grid_offset_y)
            end_pos = (grid_offset_x + x * cell_size, grid_offset_y + grid_height)
            line_color = (101, 67, 33) if x % 19 == 0 else (139, 120, 93)
            line_width = 3 if x % 19 == 0 else 1
            pygame.draw.line(self.background, line_color, start_pos, end_pos, line_width)

        for y in range(20):  # 20 lignes pour 19 cases
            start_pos = (grid_offset_x, grid_offset_y + y * cell_size)
            end_pos = (grid_offset_x + grid_width, grid_offset_y + y * cell_size)
            line_color = (101, 67, 33) if y % 19 == 0 else (139, 120, 93)
            line_width = 3 if y % 19 == 0 else 1
            pygame.draw.line(self.background, line_color, start_pos, end_pos, line_width)

        # Points de repère sur le plateau (hoshi)
        hoshi_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9), (15, 9), (3, 15), (9, 15), (15, 15)]
        for hx, hy in hoshi_points:
            hoshi_pos = (grid_offset_x + hx * cell_size, grid_offset_y + hy * cell_size)
            pygame.draw.circle(self.background, (101, 67, 33), hoshi_pos, 4)

        # Dessiner les pions avec effet 3D
        for x in range(19):
            for y in range(19):
                if board_state[y][x] != 0:
                    stone_center = (grid_offset_x + x * cell_size, grid_offset_y + y * cell_size)
                    stone_radius = cell_size // 2 - 3
                    
                    if board_state[y][x] == 1:  # Pion noir
                        # Ombre
                        pygame.draw.circle(self.background, (50, 50, 50), 
                                         (stone_center[0] + 2, stone_center[1] + 2), stone_radius)
                        # Pion principal
                        pygame.draw.circle(self.background, (20, 20, 20), stone_center, stone_radius)
                        # Reflet
                        pygame.draw.circle(self.background, (100, 100, 100), 
                                         (stone_center[0] - stone_radius//3, stone_center[1] - stone_radius//3), 
                                         stone_radius//4)
                    
                    elif board_state[y][x] == 2:  # Pion blanc
                        # Ombre
                        pygame.draw.circle(self.background, (150, 150, 150), 
                                         (stone_center[0] + 2, stone_center[1] + 2), stone_radius)
                        # Pion principal
                        pygame.draw.circle(self.background, (245, 245, 245), stone_center, stone_radius)
                        # Contour
                        pygame.draw.circle(self.background, (200, 200, 200), stone_center, stone_radius, 2)
                        # Reflet
                        pygame.draw.circle(self.background, (255, 255, 255), 
                                         (stone_center[0] - stone_radius//3, stone_center[1] - stone_radius//3), 
                                         stone_radius//4)

        # Message de statut en haut
        status_lbl = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((50, 20), (924, 50)),
            text=status_message,
            manager=self.manager,
            object_id="#status_label"
        )

        # Bouton abandonner stylisé
        abandon_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((450, 700), (124, 50)),
            text="Abandonner",
            manager=self.manager,
            object_id="#danger_btn"
        )

        pygame.display.flip()
        return abandon_btn, status_lbl, grid_offset_x, grid_offset_y

    def show_end_screen(self, is_winner, message=""):
        pygame.display.set_caption("PENTE - Fin de partie")
        self.manager.clear_and_reset()
        
        # Son de victoire ou défaite
        sound_manager.play_sound('win' if is_winner else 'lose')

        # Fond spécial pour la fin de partie
        end_background = pygame.Surface(SCREEN_SIZE)
        
        if is_winner:
            # Dégradé doré pour la victoire
            for y in range(SCREEN_HEIGHT):
                ratio = y / SCREEN_HEIGHT
                r = int(25 + 30 * (1 - ratio))
                g = int(25 + 25 * (1 - ratio))
                b = int(0 + 15 * (1 - ratio))
                color = (r, g, b)
                pygame.draw.line(end_background, color, (0, y), (SCREEN_WIDTH, y))
        else:
            # Dégradé rouge sombre pour la défaite
            for y in range(SCREEN_HEIGHT):
                ratio = y / SCREEN_HEIGHT
                r = int(40 * (1 - ratio))
                g = int(0)
                b = int(0)
                color = (r, g, b)
                pygame.draw.line(end_background, color, (0, y), (SCREEN_WIDTH, y))
        
        self.background = end_background

        # Texte principal avec animation
        result_text = "*** VICTOIRE ! ***" if is_winner else "*** DEFAITE ***"
        result_object_id = "#win_label" if is_winner else "#lose_label"

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((200, 200), (624, 80)),
            text=result_text,
            manager=self.manager,
            object_id=result_object_id
        )

        # Message du serveur ou message par défaut
        if message:
            # Utiliser le message du serveur
            display_message = message
        else:
            # Message par défaut si aucun message du serveur
            if is_winner:
                display_message = "Felicitations ! Vous avez aligne 5 pierres !"
            else:
                display_message = "Dommage ! Votre adversaire a ete plus rapide"

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((112, 300), (800, 40)),
            text=display_message,
            manager=self.manager,
            object_id="#subtitle"
        )

        # Message supplémentaire s'il y en a un (retiré car on utilise le message principal maintenant)

        # Bouton stylisé pour retourner au lobby
        return_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((412, 400), (200, 60)),
            text="<< Retour au lobby",
            manager=self.manager,
            object_id="#primary_btn"
        )

        pygame.display.flip()
        return return_btn

    def wrap_text(self, text, max_width):
        """Découpe le texte en lignes pour qu'il respecte une largeur maximale."""
        font = pygame.font.Font(None, 24)
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            if font.size(test_line)[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def update_animations(self, dt):
        """Met à jour les animations"""
        self.animation_time += dt






