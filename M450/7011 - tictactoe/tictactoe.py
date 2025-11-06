import pygame
import pygame_gui

FPS = 60

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
UI_LEFT_PANEL_WIDTH = 75
UI_LOG_TEXT_BOX_HEIGHT = 300
GRID_H_PADDING = 100
GRID_V_PADDING = 25
GRID_SIZE = 400
PARTICIPANTS = ["Human", "AI Random"]

pygame.init()

pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (5, 10), (130, 20)), text="Participant 1", manager=ui_manager)

part1 = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(
    (10, 30), (130, 40)), options_list=PARTICIPANTS,  
starting_option="Human", manager=ui_manager)

pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (5, 80), (130, 20)), text="Participant 2", manager=ui_manager)

part2 = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(
    (10, 100), (130, 40)), options_list=PARTICIPANTS,  
starting_option="Human", manager=ui_manager)


def draw_grid(screen=screen):
    cell_size = GRID_SIZE // 3
    for i in range(1, 3):
        pygame.draw.line(screen, pygame.Color('white'),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH + i * cell_size, GRID_V_PADDING),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH+ i * cell_size, GRID_V_PADDING + GRID_SIZE), 3)
        pygame.draw.line(screen, pygame.Color('white'),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH, GRID_V_PADDING + i * cell_size),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH + GRID_SIZE, GRID_V_PADDING + i * cell_size), 3)

is_running = True
while is_running:

    time_delta = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    draw_grid(screen)
    ui_manager.draw_ui(screen)

    pygame.display.flip()
    pygame.display.update()
