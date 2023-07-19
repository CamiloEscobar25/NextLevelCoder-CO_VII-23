from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import SPEED

class Speed(PowerUp):
    def __init__(self):
        selected_image = SPEED
        super().__init__(selected_image)