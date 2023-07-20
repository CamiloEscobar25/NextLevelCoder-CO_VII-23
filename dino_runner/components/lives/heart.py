from dino_runner.components.lives.life import Life
from dino_runner.utils.constants import HEART

class Heart(Life):
    def __init__(self):
        selected_image = HEART
        super().__init__(selected_image)