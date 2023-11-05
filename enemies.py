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
        self.x_pos = self.rect.centerx  # Use a separate float attribute for x position
        self.y_pos = self.rect.centery 
        self.speed = 0.2  # Adjust speed as needed

    def update(self, player_rect):
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

    def draw_enemy(self):
        # Draw the enemy on the screen
        self.screen.blit(self.image, self.rect)