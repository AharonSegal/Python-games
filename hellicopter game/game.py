import pygame
import time
from helicopter import Helicopter
from cave import Cave
from score import Score

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Helicopter Cave Game")
        
        self.helicopter = Helicopter(50, height // 2)
        self.cave = Cave(width, height, self.helicopter.rect.height * 2)
        self.score = Score()
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.gap_decrease_interval = 10
        
        self.font = pygame.font.Font(None, 36)
        self.blue = (0, 0, 255)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.reset_game()
            else:
                self.helicopter.handle_event(event)

    def update(self):
        if not self.game_over:
            self.score.update()

            if self.score.current_score > self.gap_decrease_interval:
                self.cave.decrease_gap()
                self.gap_decrease_interval += 10

            self.helicopter.update()
            self.cave.update()

            if self.check_collisions():
                self.game_over = True
                self.score.reset()

    def check_collisions(self):
        if self.helicopter.rect.top < 0 or self.helicopter.rect.bottom > self.height:
            return True
        for rect in self.cave.top + self.cave.bottom:
            if self.helicopter.rect.colliderect(rect):
                return True
        return False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.helicopter.draw(self.screen)
        self.cave.draw(self.screen)
        self.score.draw(self.screen)
        
        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()

    def draw_game_over(self):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))

        game_over_text = self.font.render("Game Over", True, self.blue)
        final_score_text = self.font.render(f"Your Time: {self.score.current_score:.1f}", True, self.blue)
        high_score_text = self.font.render(f"Best Time: {self.score.high_score:.1f}", True, self.blue)
        restart_text = self.font.render("Press SPACE to restart", True, self.blue)
        
        self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - 80))
        self.screen.blit(final_score_text, (self.width // 2 - final_score_text.get_width() // 2, self.height // 2 - 20))
        self.screen.blit(high_score_text, (self.width // 2 - high_score_text.get_width() // 2, self.height // 2 + 40))
        self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, self.height // 2 + 100))

    def reset_game(self):
        self.helicopter = Helicopter(50, self.height // 2)
        self.cave = Cave(self.width, self.height, self.helicopter.rect.height * 2)
        self.score = Score()
        self.game_over = False
        self.gap_decrease_interval = 10

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()