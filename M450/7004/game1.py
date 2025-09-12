import pygame
from pygame.locals import *
import random
import time

pygame.init()
clock = pygame.time.Clock()


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
punkte = 0
lives = 3

# Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("M450/7004/img/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        # self.surf = pygame.transform.scale(self.surf, (130,130))

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            down_sound.play()
            self.rect.move_ip(0, 5)
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
            up_sound.play()
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
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
        global punkte
        self.rect.move_ip(self.speed*-1, 0)
        if self.rect.right < 0:
            self.kill()
            punkte += 1


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


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                player.rect.right + 10,
                player.rect.centery,
            )
        )
        self.speed = 10
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


# Open Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# Create all sprites
player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

pygame.mixer.music.load("M450/7004/audio/67.mp3")
pygame.mixer.music.play(loops=-1)

up_sound = pygame.mixer.Sound("M450/7004/audio/up.ogg")
down_sound = pygame.mixer.Sound("M450/7004/audio/down.ogg")
death_sound = pygame.mixer.Sound("M450/7004/audio/deathsound.mp3")

up_sound.set_volume(0)
down_sound.set_volume(0)

# Game loop
running = True
paused = False
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_p:
                # Pause the game
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                # Pause all sprites
            if event.key == K_SPACE:
                new_bullet = Bullet()
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)
                

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
    if paused:
        continue

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    bullets.update()

    # Draw the game
    screen.fill((135, 206, 250))
    
    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Schrift und Schriftgrösse
    font = pygame.font.Font(None, 74)
    # Surface mit Schrift erzeugen. Der letzte Parameter ist die Farbe
    points = font.render("Punkte: " + str(punkte), True, (0, 0, 0))
    # Surface aif Screen blitten
    screen.blit(points, (50,10))

    # Surface mit Schrift erzeugen. Der letzte Parameter ist die Farbe
    lives_ = font.render("Leben: " + str(lives), True, (0, 0, 0))
    # Surface aif Screen blitten
    screen.blit(lives_, (550,10))

    # Update game window
    pygame.display.flip()

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        pygame.mixer.music.stop()
        up_sound.stop()
        down_sound.stop()
        death_sound.play()
        time.sleep(death_sound.get_length())
        lives -= 1
        if lives > 0:
            player = Player()
            all_sprites.add(player)
            pygame.mixer.music.play(loops=-1)
            for sprite in enemies:
                sprite.kill()
            punkte = 0
        else:
            running = False
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        punkte += 3

    clock.tick(FPS)


# Done! Time to quit.
pygame.quit()