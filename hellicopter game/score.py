import time
import pygame

class Score:
    def __init__(self):
        self.start_time = time.time()
        self.current_score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 36)
        self.color = (0, 0, 255)  # RGB value for blue

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return float(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update(self):
        self.current_score = round(time.time() - self.start_time, 1)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.save_high_score()
        self.start_time = time.time()
        self.current_score = 0

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.current_score}", True, self.color)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, self.color)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 50))