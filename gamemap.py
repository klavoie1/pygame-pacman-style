import pygame
from settings import Settings

class GameMap:
    def __init__(self, screen_width, screen_height):
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        self.cell_size = min(screen_width // len(self.map_data[0]), screen_height // len(self.map_data))
        self.map_width = len(self.map_data[0]) * self.cell_size
        self.map_height = len(self.map_data) * self.cell_size

    def is_wall(self, x, y):
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size

        return self.map_data[grid_y][grid_x] == 1

    def draw_map(self, screen):
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == 1:  # Wall
                    pygame.draw.rect(screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
