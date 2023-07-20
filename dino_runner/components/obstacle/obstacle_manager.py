import random
import pygame
from dino_runner.components.obstacle.lave import Lave
from dino_runner.components.obstacle.plant import Plant
from dino_runner.components.obstacle.bird import Bird
from dino_runner.components.obstacle.cactus import Large_Cactus, Small_Cactus
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE


class ObstacleManager:

    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)
        if game.player.rect.colliderect(self.obstacle.rect):
            if  game.player.type == SHIELD_TYPE:
                  game.player.type = DEFAULT_TYPE
            else:
                pygame.time.delay(400)
                game.playing = False

    def create_obstacle(self):
        obstacles = [Plant(), Bird(), Large_Cactus(), Small_Cactus(), Lave()]
        self.obstacle = random.choice(obstacles)
        self.has_obstacle = True


    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)