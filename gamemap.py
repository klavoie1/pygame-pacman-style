import pygame

class GameMap:
    def __init__(self):
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        self.cell_size = 40  # Adjust the cell size as needed
        self.map_width = len(self.map_data[0]) * self.cell_size
        self.map_height = len(self.map_data) * self.cell_size

    def draw_map(self, screen):
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == 1:  # Example: 1 represents a wall, 0 represents a path
                    pygame.draw.rect(screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    # Adjust the colors, dimensions, and cell types as needed