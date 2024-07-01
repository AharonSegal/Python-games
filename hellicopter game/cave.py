import pygame
import random

class Cave:
    def __init__(self, width, height, min_gap_size):
        self.width = width
        self.height = height
        self.cave_width = 50
        self.min_gap_size = min_gap_size
        self.cave_gap = max(300, min_gap_size * 2)
        self.gap_decrease = 10
        self.top = []
        self.bottom = []
        self.generate_cave()

    def generate_cave(self):
        x = self.width
        while x < self.width * 2:
            top_y = random.randint(50, self.height - self.cave_gap - 50)
            self.top.append(pygame.Rect(x, 0, self.cave_width, top_y))
            self.bottom.append(pygame.Rect(x, top_y + self.cave_gap, self.cave_width, self.height - top_y - self.cave_gap))
            x += self.cave_width

    def update(self):
        for rect in self.top + self.bottom:
            rect.x -= 2

        if self.top[0].right < 0:
            self.top.pop(0)
            self.bottom.pop(0)
            top_y = random.randint(50, self.height - self.cave_gap - 50)
            self.top.append(pygame.Rect(self.top[-1].right, 0, self.cave_width, top_y))
            self.bottom.append(pygame.Rect(self.bottom[-1].right, top_y + self.cave_gap, self.cave_width, self.height - top_y - self.cave_gap))

    def decrease_gap(self):
        self.cave_gap = max(self.cave_gap - self.gap_decrease, self.min_gap_size * 2)

    def draw(self, screen):
        for rect in self.top + self.bottom:
            pygame.draw.rect(screen, (255, 255, 255), rect)