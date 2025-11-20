"""
Sie implementieren ein kleines Python-Programm mit pygame und pygame_gui, das das MVC-Prinzip in einer sehr einfachen Form verwendet.

Erstellen Sie eine Klasse Box als Model, die eine Farbe hat und diese in eine zufällige Farbe ändern kann.

Erstellen Sie eine Klasse BoxView die im Konstruktor ein Box-Objekt erhält. Sie soll eine Methode zeichne(surface) besitzen, die ein Rechteck-Model mit zeichnet

Das Gui soll ein Button "Farbe ändern" besitzen. Wenn dieser gedrückt wird, dann soll das Rechteck eine zufällige Farbe annehmen.
"""
import pygame
import pygame_gui

import random

class Box:
    def __init__(self, color):
        self.color = color

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class BoxView:
    def __init__(self, box):
        self.box = box

    def draw(self, surface):
        pygame.draw.rect(surface, self.box.color, pygame.Rect(250, 200, 100, 100))

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MVC Box Color Changer')
clock = pygame.time.Clock()
ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
change_color_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 350), (100, 50)),
                                                     text='Farbe ändern',
                                                     manager=ui_manager)
box = Box((255, 0, 0))
box_view = BoxView(box)
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == change_color_button:
                    box.change_color()

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.fill((0, 0, 0))
    box_view.draw(screen)
    ui_manager.draw_ui(screen)

    pygame.display.update()