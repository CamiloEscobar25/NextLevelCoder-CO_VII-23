from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import HAMMER

class Hammer(PowerUp):
    def __init__(self):
        selected_image = HAMMER
        super().__init__(selected_image)