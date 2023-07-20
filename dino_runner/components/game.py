import pygame
import random

from dino_runner.components.obstacle.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.powerup_manager import PowerUpManager
from dino_runner.utils.constants import  BG_city, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacle.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.powerup_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Dinosaur()
        self.cloud_list = pygame.sprite.Group()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.score = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        for i in range(7):
            CLOUD = Cloud()
            CLOUD.rect.x = random.randint(0, 1100)
            CLOUD.rect.y = random.randint(20, 50)
            self.cloud_list.add(CLOUD)
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(pygame.key.get_pressed())
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self)
        self.increase_score()
        for cloud in self.cloud_list:
            cloud.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud_list.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def increase_score(self):
        self.score += 1

    def draw_background(self):
        image_width = BG_city.get_width()
        self.screen.blit(BG_city, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG_city, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG_city, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed