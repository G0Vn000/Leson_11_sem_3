import pygame


class Block:
    """Прямоугольник"""

    def __init__(self, width, height, color=(0, 0, 0)):
        self.surface = pygame.Surface((width, height))
        self.width, self.height = width, height
        self.color = color
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect()

    def set_color(self, new_color):
        """Задать цвет (перекрасить блок)"""
        self.color = new_color
        self.surface.fill(self.color)

    def set_position(self, x: int, y: int = None):
        """Задать положение блока"""
        self.rect.x = x
        if y is not None:
            self.rect.y = y


    def get_position(self):
        return self.rect.x, self.rect.y
