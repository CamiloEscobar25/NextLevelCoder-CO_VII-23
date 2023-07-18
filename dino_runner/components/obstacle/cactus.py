import random
from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Large_Cactus(Obstacle):
    def __init__(self):
        image_list = LARGE_CACTUS
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        self.rect.y = 430

class Small_Cactus(Obstacle):
    def __init__(self):
        image_list = SMALL_CACTUS
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        self.rect.y = 455