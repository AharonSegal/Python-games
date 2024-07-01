import pygame
import math

class Helicopter:
    def __init__(self, x, y):
        self.image = self.create_helicopter_surface(40, 20)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 0
        self.propeller_angle = 0

    def create_helicopter_surface(self, width, height):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(surface, (255, 255, 255), (10, 7, 30, 13))
        pygame.draw.line(surface, (255, 255, 255), (10, 13), (2, 13), 2)
        pygame.draw.line(surface, (255, 255, 255), (2, 8), (2, 18), 2)
        pygame.draw.line(surface, (255, 255, 255), (25, 7), (25, 5), 2)
        pygame.draw.line(surface, (255, 255, 255), (0, 13), (2, 13), 2)
        return surface

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.speed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.speed = 2

    def update(self):
        self.rect.y += self.speed
        self.propeller_angle += 30

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        main_prop_x = self.rect.x + 25
        main_prop_y = self.rect.y + 5
        tail_prop_x = self.rect.x + 2
        tail_prop_y = self.rect.y + 13
        
        pygame.draw.line(screen, (255, 255, 255), 
                         (main_prop_x + 15 * math.cos(math.radians(self.propeller_angle)), 
                          main_prop_y + 15 * math.sin(math.radians(self.propeller_angle))),
                         (main_prop_x + 15 * math.cos(math.radians(self.propeller_angle + 180)), 
                          main_prop_y + 15 * math.sin(math.radians(self.propeller_angle + 180))), 2)
        
        pygame.draw.line(screen, (255, 255, 255), 
                         (tail_prop_x + 5 * math.cos(math.radians(self.propeller_angle)), 
                          tail_prop_y + 5 * math.sin(math.radians(self.propeller_angle))),
                         (tail_prop_x + 5 * math.cos(math.radians(self.propeller_angle + 180)), 
                          tail_prop_y + 5 * math.sin(math.radians(self.propeller_angle + 180))), 2)