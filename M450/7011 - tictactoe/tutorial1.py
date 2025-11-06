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


hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                             (350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=ui_manager)

byebye_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                             (350, 350), (100, 50)),
                                             text='Say ByeBye',
                                             manager=ui_manager)



is_running = True
while is_running:
    time_delta = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                 pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(100, 100, 200, 300),
           html_message="Hello World!",
           manager=ui_manager)
            if event.ui_element == byebye_button:
                pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(100, 100, 200, 300),
           html_message="Bye Bye World!",
           manager=ui_manager)

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    ui_manager.draw_ui(screen)

    pygame.display.flip()
