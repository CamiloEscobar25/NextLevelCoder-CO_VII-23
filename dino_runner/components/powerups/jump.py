from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import JUMP

class Jump(PowerUp):
    def __init__(self):
        selected_image = JUMP
        super().__init__(selected_image)