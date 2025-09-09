import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("M450/7004/img/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255)) 
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("M450/7004/img/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 10, # rect.right - rect.centerx = 10
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    def update(self):
            self.rect.move_ip(self.speed*-1, 0)
            if self.rect.right < 0:
                self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("M450/7004/img/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
                center=(
                    SCREEN_WIDTH + 50, # rect.right - rect.centerx = 50
                    random.randint(0, SCREEN_HEIGHT),
                )
            )

    # Move the sprite based on speed
    def update(self):
            self.rect.move_ip(-5, 0)
            if self.rect.right < 0:
                self.kill()


# Open Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# Create all sprites
player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Game loop
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            # Create the new enemy, and add it to our sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

            
    # Gamelogic comes here


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    # Draw the game
    screen.fill((135, 206, 250))
    
    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update game window
    pygame.display.flip()
    clock.tick(FPS)


# Done! Time to quit.
pygame.quit()