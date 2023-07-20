from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    DEFAULT_TYPE,
    SCREEN_WIDTH
)

class PowerUp(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 40
        self.rect.y = 325
        self.type = DEFAULT_TYPE

    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x > 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)