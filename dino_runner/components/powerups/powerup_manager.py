import random
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.jump import Jump
from dino_runner.components.powerups.speed import Speed

class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100

    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
            self.next_powerup_show += 100
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False

    def create_powerup(self):
        powerups = [Hammer(), Shield(), Speed(), Jump()]
        self.powerup = random.choice(powerups)
        self.has_powerup = True


    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)