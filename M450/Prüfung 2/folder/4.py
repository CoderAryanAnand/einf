"""
Schreiben Sie ein Autorennspiel in dem ein Rennauto am unteren Bildschirmrand plaziert wird.

Später soll das Auto auf einer von drei Spuren fahren: links, Mitte oder rechts. Für diese Aufgabe können Sie es in der linken Spur plazieren.

Von oben kommen andere Autos mit unterschiedlichen Geschwindigkeiten, zufällig auf die drei Spuren verteilt, angefahren.

Um eine Illusion von "Fahren" zu erzeugen, sollen am Strassenrand Bäume zufällig plaziert werden und sich mit gleicher Geschwindigkeit von oben nach unten bewegen.

Das Spiel sollte so aussehen:
"""

import pygame
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
FPS = 60

BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
BLACK = (0,0,0)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("car!")
clock = pygame.time.Clock()

class CarPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load("Grafiken/player.png").convert()
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.rect.bottom = SCREEN_HEIGHT / 2
        self.speedx = 0


class CarEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    
        self.image = pygame.image.load("Grafiken/enemy.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 300)
        self.rect.y = -20
        self.speedx = random.randrange(-3, -1)

    def update(self):
        self.rect.y -= self.speedx
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.x = random.randrange(100, 300)
            self.rect.y = -20

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Grafiken/tree.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 300)
        self.rect.y = -20
        self.speedx = random.randrange(-3, -1)

    def update(self):
        self.rect.y -= self.speedx
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.x = random.randrange(100, 300)
            self.rect.y = -20




all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

carp = CarPlayer()
all_sprites.add(carp)

for mines in range(8):
    tree = Tree()
    all_sprites.add(tree)
    all_sprites.add(tree)

    care = CarEnemy()
    all_sprites.add(care)
    mobs.add(care)



# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()



    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
