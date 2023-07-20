import random
from dino_runner.components.lives.heart import Heart

class LifeManager:
    def __init__(self):
        self.has_life = False
        self.life = None
        self.next_life_show = 300
        self.can_create_life = True

    def update(self, game):

        if not self.has_life and game.score >= self.next_life_show and self.can_create_life:
            self.create_life()
            self.next_life_show += random.randint(200, 500)
        if self.has_life:
            self.has_life = self.life.update(game.game_speed)
            if game.player.rect.colliderect(self.life.rect):
                self.has_life = False
                game.add_life()
                if game.current_lives >= game.max_lives:
                    self.can_create_life = False
                else: 
                    self.can_create_life = True

    def create_life(self):
        self.life = Heart()
        self.has_life = True

    def draw(self, screen):
        if self.has_life:
            self.life.draw(screen)