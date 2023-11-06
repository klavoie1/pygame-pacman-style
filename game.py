import pygame
from settings import Settings
from player import Player
from enemies import Enemy
from gamemap import GameMap

class PacmanGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pac-Man Game")

        # Creating instances of player and enemies
        self.player = Player(self.screen)
        self.enemies = [Enemy(self.screen, 100, 100), Enemy(self.screen, 200, 200)]  # Example: 2 enemies
        self.game_map = GameMap(self.settings.screen_width, self.settings.screen_height)


    def run_game(self):
        running = True
        while running:
            self.screen.fill(self.settings.bg_color)  # Fill for the screen background

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.player.handle_events(event)

            self.player.update(self.game_map)
            self.player.draw_player()

            for enemy in self.enemies:
                enemy.update(self.player.rect, self.game_map)
                enemy.draw_enemy()

            self.game_map.draw_map(self.screen)

            pygame.display.flip()  # Updating the screen

    def start(self):
        self.run_game()

if __name__ == "__main__":
    game = PacmanGame()
    game.start()