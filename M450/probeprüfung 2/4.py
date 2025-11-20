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
pygame.display.set_caption("Submarine!")
clock = pygame.time.Clock()

class Submarine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load("M450/7010/asteroids/asteroids/img/playerShip1_orange.png").convert()
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.rect.bottom = SCREEN_HEIGHT / 2
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def go_up_down(self, dir):
        if dir in [pygame.K_UP, pygame.K_DOWN]:
            if dir == pygame.K_DOWN and self.rect.bottom < 450:

                self.rect.bottom += 150 
            if dir == pygame.K_UP and self.rect.bottom > 150:
                self.rect.bottom -= 150 


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        meteor_images = []
        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
               'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
       
        for img in meteor_list:
            meteor_images.append(pygame.image.load("M450/7010/asteroids/asteroids/img/"+img).convert()) 

        self.image = random.choice(meteor_images)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randrange(0, SCREEN_HEIGHT)
        self.speedx = random.randrange(-3, -1)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < -25:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randrange(0, SCREEN_HEIGHT)

class Mine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        meteor_images = []
        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
               'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
       
        for img in meteor_list:
            meteor_images.append(pygame.image.load("M450/7010/asteroids/asteroids/img/"+img).convert()) 

        self.image = random.choice(meteor_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = 0
        self.speedy = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.x = random.randrange(0, SCREEN_WIDTH)
            self.rect.y = 0

class Bubble(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        meteor_images = []
        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
               'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
       
        for img in meteor_list:
            meteor_images.append(pygame.image.load("M450/7010/asteroids/asteroids/img/"+img).convert()) 

        self.image = random.choice(meteor_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT)
        self.speedy = random.randrange(-3, -1)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < 0:
            self.rect.x = random.randrange(0, SCREEN_WIDTH)
            self.rect.y = random.randrange(0, SCREEN_HEIGHT)

# Load background graphics
background = pygame.image.load("M450/7010/asteroids/asteroids/img/starfield.png").convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

submarine = Submarine()
all_sprites.add(submarine)

for mines in range(8):
    mine = Mine()
    all_sprites.add(mine)
    mobs.add(mine)

    fish = Fish()
    all_sprites.add(fish)
    mobs.add(fish)

    bubble = Bubble()
    all_sprites.add(bubble)


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
        if event.type == pygame.KEYDOWN:
            submarine.go_up_down(event.key)

    # Update
    all_sprites.update()



    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
