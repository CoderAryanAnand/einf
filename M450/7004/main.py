import pygame
from pygame.locals import *
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Open Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unser erstes Pygame-Spiel")


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
            
    # Gamelogic comes here
    # Draw the game
    screen.fill((135, 206, 250))
    ### HIER Surfaces einfuegen ###
    surf_red = pygame.Surface((100, 100))
    surf_red.fill((255, 0, 0))
    screen.blit(surf_red, (350, 250))

    surf_jet = pygame.image.load("M450/7004/img/jet.png").convert()
    surf_jet.set_colorkey((255, 255, 255))  # Weiß als transparent setzen
    screen.blit(surf_jet, (200, 150))

    surf_missile = pygame.image.load("M450/7004/img/missile.png").convert()
    surf_missile.set_colorkey((255, 255, 255))
    screen.blit(surf_missile, (500, 400))

    surf_cloud = pygame.image.load("M450/7004/img/cloud.png").convert()
    surf_cloud.set_colorkey((255, 255, 255))
    screen.blit(surf_cloud, (100, 50))
    # Update game window
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
