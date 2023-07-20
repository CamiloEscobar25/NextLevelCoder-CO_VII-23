from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

class Life(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
        self.rect.y = 325

    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x > - self.rect.width
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)