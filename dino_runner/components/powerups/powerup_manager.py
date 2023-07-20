import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.jump import Jump
from dino_runner.components.powerups.speed import Reset_Speed
from dino_runner.utils.constants import SOUND_POWERUP

class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100
        self.powerup_sound = pygame.mixer.Sound(SOUND_POWERUP)

    def apply_powerup_effect(self, game):
        if isinstance(self.powerup, Reset_Speed):
            game.game_speed = 20
        elif isinstance(self.powerup, Jump):
            game.player.activate_jump_boost()

        if game.player.rect.colliderect(self.powerup.rect):
            self.has_powerup = False
            game.player.type = self.powerup.type

    def update(self, game):
        if not self.has_powerup and game.score >= self.next_powerup_show:
            self.create_powerup()
            self.next_powerup_show += random.randint(200, 500)
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False
                game.player.type = self.powerup.type
                self.apply_powerup_effect(game)
                self.play_powerup_sound()

    def create_powerup(self):
        powerups = [Shield(), Jump(), Reset_Speed()]
        self.powerup = random.choice(powerups)
        self.has_powerup = True
        

    def play_powerup_sound(self):
        self.powerup_sound.play()

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
