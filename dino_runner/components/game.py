import pygame
import random

from dino_runner.components.obstacle.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.powerup_manager import PowerUpManager
from dino_runner.utils.constants import  BG_city, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SOUND_JUMP, SOUND_POWERUP, SOUND_DEAD, SOUND_BACKGROUND
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacle.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.powerup_manager import PowerUpManager
from dino_runner.components.lives.life_manager import LifeManager
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.max_speed = 50
        self.speed_increase_interval = 500
        self.speed_increase_amount = 10
        self.speed_increase_counter = 0 
        self.x_pos_bg = 0
        self.y_pos_bg = -20
        self.player = Dinosaur()
        self.cloud_list = pygame.sprite.Group()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()
        self.life_manager = LifeManager()
        self.current_score = 0
        self.max_score = self.load_max_score()
        self.score = 0
        self.max_lives = 5
        self.current_lives = 3

        pygame.mixer.init()
        self.jump_sound = pygame.mixer.Sound(SOUND_JUMP)
        self.powerup_sound = pygame.mixer.Sound(SOUND_POWERUP)
        self.dead_sound = pygame.mixer.Sound(SOUND_DEAD)
        self.background_music = pygame.mixer.Sound(SOUND_BACKGROUND)
        self.background_music.play(-1)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.current_lives = 3

        for i in range(7):
            CLOUD = Cloud()
            CLOUD.rect.x = random.randint(0, 1100)
            CLOUD.rect.y = random.randint(20, 50)
            self.cloud_list.add(CLOUD)
        while self.current_lives > 0 and self.playing:
            self.events()
            self.update()
            self.draw()

            self.speed_increase_counter += 1
            if self.speed_increase_counter >= self.speed_increase_interval and self.game_speed < self.max_speed:
                self.game_speed += self.speed_increase_amount
                self.speed_increase_counter = 0

            if self.current_lives == 0:
                self.game_over()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(pygame.key.get_pressed(), self)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self)
        self.life_manager.update(self)
        self.increase_score()

        if self.obstacle_manager.has_obstacle and self.player.rect.colliderect(self.obstacle_manager.obstacle.rect):
            if self.player.type == SHIELD_TYPE:
                self.player.type = DEFAULT_TYPE
            elif self.current_lives > 1:
                self.current_lives -= 1
                self.life_manager.can_create_life = True
                pygame.time.delay(500)

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
        self.draw_lives()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_lives(self):
        self.font = pygame.font.SysFont(None, 40)
        lives_text = self.font.render(f"Lives: {self.current_lives}", True, (0, 0, 0))
        self.screen.blit(lives_text, (10, 90))

    def add_life(self):
        if self.current_lives < self.max_lives:
            self.current_lives +=1

    def draw_score(self):
        self.font = pygame.font.SysFont(None, 40)
        current_score_text = self.font.render(f"Score: {self.current_score}", True, (0, 0, 0))
        max_score_text = self.font.render(f"Max Score: {self.max_score}", True, (0, 0, 0))
        self.screen.blit(current_score_text, (10, 10))
        self.screen.blit(max_score_text, (10, 50))

    def load_max_score(self):
        try:
            with open('max_score.txt', 'r') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_max_score(self):
        with open('max_score.txt', 'w') as f:
            f.write(str(self.max_score))

    def increase_score(self):
        self.score += 1
        self.current_score = self.score
        if self.score > self.max_score:
          self.max_score = self.score
          self.save_max_score()

    def draw_background(self):
        image_width = BG_city.get_width()
        self.screen.blit(BG_city, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG_city, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG_city, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed