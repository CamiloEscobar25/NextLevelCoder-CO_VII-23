from dino_runner.utils.constants import PLANT
from dino_runner.components.obstacle.obstacle import Obstacle

class Plant(Obstacle):
    def __init__(self):
        self.images = PLANT
        self.index = 0
        self.image = self.images[self.index // 5]
        super().__init__(self.image)
        self.rect.y = 440
   
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        self.image = self.images[self.index // 5]
        screen.blit(self.image, self.rect)
        self.index += 1