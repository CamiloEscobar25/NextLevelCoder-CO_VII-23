import pygame
import random
from dino_runner.utils.constants import CLOUD

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = CLOUD
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -300:
            self.rect.x = 1100
            self.rect.y = random.randrange(15)