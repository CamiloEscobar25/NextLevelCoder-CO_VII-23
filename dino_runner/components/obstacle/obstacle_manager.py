import random
import pygame
from dino_runner.components.obstacle.lave import Lave
from dino_runner.components.obstacle.plant import Plant
from dino_runner.components.obstacle.bird import Bird
from dino_runner.components.obstacle.cactus import Large_Cactus, Small_Cactus
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, SOUND_DAMAGE, SOUND_DEAD


class ObstacleManager:
    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None
        pygame.mixer.init()
        self.damge_sound = pygame.mixer.Sound(SOUND_DAMAGE)
        self.dead_sound = pygame.mixer.Sound(SOUND_DEAD)

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)

        if game.player.rect.colliderect(self.obstacle.rect):
            self.damge_sound.play()
            if game.player.type == SHIELD_TYPE:
                self.has_obstacle = False
                game.player.type = DEFAULT_TYPE
            elif game.current_lives > 1:
                game.current_lives -= 1
                self.has_obstacle = False
                self.obstacle = None
                game.life_manager.can_create_life = True
            else:
                pygame.time.delay(500)
                self.dead_sound.play()
                pygame.time.delay(1000)
                game.playing = False

    def create_obstacle(self):
        obstacles = [Plant(), Bird(), Large_Cactus(), Small_Cactus(), Lave()]
        self.obstacle = random.choice(obstacles)
        self.has_obstacle = True

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)
