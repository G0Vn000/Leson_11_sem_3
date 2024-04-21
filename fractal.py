"""фрактал "H-дерево" """
import random

import pygame
from pygame.event import Event

from tools import Block


class Window:
    base_color = (155, 155, 200)
    red_color = (200, 155, 155)
    green_color = (155, 200, 155)
    """Окно программы"""

    def __init__(self, width=800, height=600):
        self._running = None
        self.i = None
        pygame.init()
        self.width, self.height = width, height
        self._surf_color = (0, 0, 0)  # Цвет заливки рабочей поверхности
        self.line_length = 200
        self.depth = 6
        self._display_surf = pygame.display.set_mode((self.width, self.height))  # Рабочая поверхность
        self._display_surf.fill(self._surf_color)  # Окрашиваем рабочую поверхность цветом заливки
        self._clock = pygame.time.Clock()
        self.lines: list[Block] = []

    def draw_h_tree(self, x: int, y: int, line_lenght: int, depth):
        if depth == 0:
            return
        h_line = Block(line_lenght, 5, self.base_color)
        v1_line = Block(5, line_lenght, self.base_color)
        v2_line = Block(5, line_lenght, self.base_color)

        x0 = x - line_lenght // 2
        x1 = x + line_lenght // 2
        y0 = y - line_lenght // 2
        y1 = y + line_lenght // 2

        h_line.set_position(x0, y)
        v1_line.set_position(x0, y0)
        v2_line.set_position(x1, y0)

        self.lines.append(h_line)
        self.lines.append(v1_line)
        self.lines.append(v2_line)

        self.draw_h_tree(x0, y0, line_lenght // 2, depth - 1)
        self.draw_h_tree(x1, y0, line_lenght // 2, depth - 1)
        self.draw_h_tree(x1, y1, line_lenght // 2, depth - 1)
        self.draw_h_tree(x0, y1, line_lenght // 2, depth - 1)

    def on_loop(self):
        start_x = self.width // 2
        start_y = self.height // 2
        self.draw_h_tree(start_x, start_y, self.line_length, self.depth)

    def on_event(self, event: Event):
        if event.type == pygame.QUIT:
            self._running = False

    def render(self):
        self._display_surf.fill(self._surf_color)
        for line in self.lines:
            self._display_surf.blit(line.surface, line.rect)
        pygame.display.flip()

    def run(self):
        self._running = True
        while self._running:
            self._clock.tick(2)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.render()
        pygame.quit()


my_window = Window(800, 800)
my_window.run()
