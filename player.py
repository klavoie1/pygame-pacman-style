import pygame
from gamemap import GameMap

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface((30, 30)) # Creates a little square for the player
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()

        # Initial position of the player
        self.rect.centerx = screen.get_rect().centerx
        self.rect.centery = screen.get_rect().centery

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.x_pos = self.rect.centerx
        self.y_pos = self.rect.centery
        self.speed = 0.3

    def check_collision(self, x, y, game_map):
        # Check for collisions with walls
        player_rect = pygame.Rect(self.rect)
        player_rect.x = x
        player_rect.y = y

        for row in game_map.map_data:
            for wall in row:
                if wall == 1:
                    wall_rect = pygame.Rect(row.index(wall) * game_map.cell_size, game_map.map_data.index(row) * game_map.cell_size, game_map.cell_size, game_map.cell_size)
                    if player_rect.colliderect(wall_rect):
                        return True  # Collision detected

        return False  # No collision

    def update(self, game_map):
        # Update player position based on movement flags
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.speed
        if self.moving_down and self.rect.bottom < self.screen.get_height():
            self.y_pos += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.speed
        if self.moving_right and self.rect.right < self.screen.get_width():
            self.x_pos += self.speed

        self.rect.centerx = int(self.x_pos)
        self.rect.centery = int(self.y_pos)

        # Update player position based on movement flags and collision detection
        if self.moving_up and self.rect.top > 0 and not self.check_collision(self.rect.x, self.rect.y - self.speed, game_map):
            self.rect.y -= self.speed

        # Need to implement similar collision detection for other directions

    def draw_player(self):
        # Draw the player on the screen
        self.screen.blit(self.image, self.rect)

    def handle_events(self, event):
        # Handles keyboard presses for player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.moving_up = True
            elif event.key == pygame.K_a:
                self.moving_left = True
            elif event.key == pygame.K_s:
                self.moving_down = True
            elif event.key == pygame.K_d:
                self.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.moving_up = False
            elif event.key == pygame.K_a:
                self.moving_left = False
            elif event.key == pygame.K_s:
                self.moving_down = False
            elif event.key == pygame.K_d:
                self.moving_right = False
