import pygame
import os

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (1).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (2).png")),
    ]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (5).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (6).png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (3).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Run (4).png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Jump (1).png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Jump (3).png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Jump (2).png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (1).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (2).png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (5).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (6).png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (3).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino 2/Duck (4).png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

PLANT = [
    pygame.image.load(os.path.join(IMG_DIR, 'Plant/Plant-1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Plant/Plant-2.png')),  
]

LAVE = [
    pygame.image.load(os.path.join(IMG_DIR, 'Lave/Lave-1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Lave/Lave-2.png')),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
JUMP = pygame.image.load(os.path.join(IMG_DIR, 'Other/Jump.png'))
SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/Speed.png'))

BG_city = pygame.image.load(os.path.join(IMG_DIR, 'Other/BGcity.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
