# --- SCHUMMELZETTEL 2: PYGAME SPRITES & COLLISION (Based on 4.py, asteroids.py, game1.py) ---
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 1. Sprite Klasse (Goal 14, 15)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Wichtig: Parent Konstruktor aufrufen!
        # Bild laden (z.B. aus game1.py / 4.py)
        self.image = pygame.Surface((50, 40)) 
        self.image.fill((0, 255, 0)) # Green square placeholder
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        # Tastatur Eingabe (Continuous Movement - game1.py Style)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            
        # Bildschirm Grenzen (Boundaries - 4.py Style)
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # Schießen Logik (asteroids.py Style)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        # Zufällige Position (asteroids.py / 4.py Style)
        self.rect.x = random.randrange(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(2, 6)

    def update(self):
        self.rect.y += self.speed_y
        # Reset wenn unten raus (Infinite Loop logic)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - 30)
            self.rect.y = random.randrange(-100, -40)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill() # Entfernt Sprite aus allen Gruppen

# --- SETUP ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Gruppen (Wichtig für Kollisionen!)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Enemies spawnen
for i in range(5):
    m = Enemy()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # --- KOLLISIONEN (CRITICAL PART for asteroids.py / game1.py) ---
    
    # 1. Bullet trifft Enemy (groupcollide)
    # True, True = Beide Sprites werden gelöscht (Bullet und Enemy)
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        # Neuen Enemy spawnen (damit sie nicht ausgehen)
        m = Enemy()
        all_sprites.add(m)
        mobs.add(m)
        print("Enemy Hit! +Score")

    # 2. Enemy trifft Player (spritecollide)
    # False = Mob wird NICHT gelöscht (in asteroids.py wäre es True/False je nach Logik)
    hits_player = pygame.sprite.spritecollide(player, mobs, False)
    if hits_player:
        print("Player died!")
        running = False 

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()