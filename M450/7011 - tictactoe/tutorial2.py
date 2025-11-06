import pygame
import pygame_gui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))


doit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                             (350, 350), (100, 50)),
                                             text='Do it!',
                                             manager=ui_manager)

number_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((310, 270), (70, 50)),
                                                    manager=ui_manager)

entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((410, 270), (70, 50)),
                                                    manager=ui_manager)

number_entry.set_allowed_characters('numbers')


is_running = True
while is_running:
    time_delta = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == doit_button:
                text = entry.get_text()
                number = int(number_entry.get_text())
                message = number * f"{text}\n"
                pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(100, 100, 200, 300),
                html_message=f"{message}",
                manager=ui_manager)

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    ui_manager.draw_ui(screen)

    pygame.display.flip()
