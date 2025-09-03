import pygame
from pygame.locals import *

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Open Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ein komisches Gesicht in Pygame")

# Game loop
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE or event.key == K_BACKSPACE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    # Gamelogic comes here
    # Draw the game
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (200, 150), 100)
    pygame.draw.circle(screen, (255, 0, 0), (600, 150), 100)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(300, 300, 200, 100))
    # Update game window
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
