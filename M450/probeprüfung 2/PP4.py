import pygame
from pygame.locals import *
from random import *

FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ENEMY_MAX = 6
BUBBLE_MAX = 10

pygame.init()
pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__() 
        self.surf =  pygame.Surface((50, 50))
        self.surf.fill("yellow")
        self.rect = self.surf.get_rect(  center=(
        SCREEN_WIDTH/2,
        SCREEN_HEIGHT-60
    ))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.speed = randint(2, 5)
        self.surf = pygame.Surface((40, 30))
        self.surf.fill("orange")
        self.rect = self.surf.get_rect(
    center=(
        randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
        randint(0, SCREEN_HEIGHT),
    )
)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb, self).__init__()
        self.speed = randint(2, 5)
        self.surf = pygame.Surface((40, 40))
        self.surf.fill("black")
        self.rect = self.surf.get_rect(
    center=(
        randint(0, SCREEN_WIDTH),
        randint(-SCREEN_HEIGHT, 0),
    )
)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        super(Bubble, self).__init__()
        self.surf = pygame.Surface((10, 10 ))
        self.surf.fill("blue")
        self.rect = self.surf.get_rect(
    center=(
        randint(0, SCREEN_WIDTH),
        randint(SCREEN_HEIGHT, SCREEN_HEIGHT*2),
    )
)

    def update(self):
        self.rect.move_ip(0, -3)
        if self.rect.top < 0:
            self.kill()


def create(enemies, bombs, bubbles):
   
    # Spawn enemies until max
    while len(enemies) < ENEMY_MAX:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
    while len(bombs) < ENEMY_MAX:
        new_bomb = Bomb()
        bombs.add(new_bomb)
        all_sprites.add(new_bomb)
    while len(bubbles) < BUBBLE_MAX:
        new_bubble = Bubble()
        bubbles.add(new_bubble)
        all_sprites.add(new_bubble)
  
player = Player()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bombs = pygame.sprite.Group()
bubbles = pygame.sprite.Group()

all_sprites.add(player)
is_running = True
while is_running:
    time_delta = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    enemies.update()
    bombs.update()
    bubbles.update()
    create(enemies, bombs, bubbles)

    screen.fill(pygame.Color("#0BA1E1"))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()