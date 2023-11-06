import pygame
import random

class Enemy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.Surface((30, 30)) # Creates a little square for the player
        self.image.fill((100, 100, 0))
        self.rect = self.image.get_rect()

        # Set the initial position for the enemy
        self.rect.centerx = screen.get_rect().centerx
        self.rect.centery = screen.get_rect().centery

        # Enemy movement speed
        self.x_pos = self.rect.centerx 
        self.y_pos = self.rect.centery 
        self.speed = 0.2

    def check_collision(self, x, y, game_map):
        # Check for collisions with walls
        enemy_rect = pygame.Rect(self.rect)
        enemy_rect.x = x
        enemy_rect.y = y

        for row in game_map.map_data:
            for wall in row:
                if wall == 1:
                    wall_rect = pygame.Rect(row.index(wall) * game_map.cell_size, game_map.map_data.index(row) * game_map.cell_size, game_map.cell_size, game_map.cell_size)
                    if enemy_rect.colliderect(wall_rect):
                        return True  # Collision detected

        return False  # No collision

    def update(self, player_rect, game_map):
        # Implement enemy behavior with fractional movement
        if self.rect.centerx < player_rect.centerx:
            self.x_pos += self.speed
        elif self.rect.centerx > player_rect.centerx:
            self.x_pos -= self.speed

        if self.rect.centery < player_rect.centery:
            self.y_pos += self.speed
        elif self.rect.centery > player_rect.centery:
            self.y_pos -= self.speed

        # Update the integer rect based on the fractional position
        self.rect.centerx = int(self.x_pos)
        self.rect.centery = int(self.y_pos)

        # Implement enemy behavior with collision detection
        if self.rect.centerx < player_rect.centerx and not self.check_collision(self.rect.x + self.speed, self.rect.y, game_map):
            self.rect.x += self.speed
        # Need to implement similar collision detection for other directions

    def draw_enemy(self):
        # Draw the enemy on the screen
        self.screen.blit(self.image, self.rect)