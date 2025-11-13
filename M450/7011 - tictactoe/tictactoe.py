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
PARTICIPANTS = ("Human", "AI Random")

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

pos = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (0, 250), (130, 20)), text="0, 0", manager=ui_manager)

part2 = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(
    (10, 100), (130, 40)), options_list=PARTICIPANTS,  
starting_option="Human", manager=ui_manager)

restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (10, 160), (130, 40)), text="Restart", manager=ui_manager)

positions_of_grid_cells = [[(175, 25), (310, 25), (440, 25)],
                           [(175, 160), (310, 160), (440, 160)],
                           [(175, 290), (310, 290), (440, 290)]]

def draw_grid(screen=screen):
    cell_size = GRID_SIZE // 3
    for i in range(1, 3):
        pygame.draw.line(screen, pygame.Color('white'),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH + i * cell_size, GRID_V_PADDING),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH+ i * cell_size, GRID_V_PADDING + GRID_SIZE), 3)
        pygame.draw.line(screen, pygame.Color('white'),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH, GRID_V_PADDING + i * cell_size),
                         (GRID_H_PADDING + UI_LEFT_PANEL_WIDTH + GRID_SIZE, GRID_V_PADDING + i * cell_size), 3)
    for y in range(0,3):
        for x in range(0,3):
            if tic_tac_toe_grid[y][x] == 1:
                # draw image x from img folder
                x_img = pygame.image.load('M450/7011 - tictactoe/img/x.png')
                x_img = pygame.transform.scale(x_img, (cell_size - 20, cell_size - 20))
                position = positions_of_grid_cells[y][x]
                screen.blit(x_img, position)
            elif tic_tac_toe_grid[y][x] == 2:
                # draw image o from img folder
                o_img = pygame.image.load('M450/7011 - tictactoe/img/o.png')
                o_img = pygame.transform.scale(o_img, (cell_size - 20, cell_size - 20))
                position = positions_of_grid_cells[y][x]
                screen.blit(o_img, position)
                

tic_tac_toe_grid = [[0 for _ in range(3)] for _ in range(3)]

def get_grid_pos(mouse_pos):
    x, y = mouse_pos
    row, col = -1, -1
    if 175 < x < 575 and 25 < y < 425:
        if x < 310:
            col = 0
        elif x < 440:
            col = 1
        else:
            col = 2
        if y < 160:
            row = 0
        elif y < 290:
            row = 1
        else:
            row = 2
    return row, col
    

is_running = True
player_turn = 1

while is_running:

    time_delta = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        ui_manager.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos.set_text(str(pygame.mouse.get_pos()))
            y, x = get_grid_pos(pygame.mouse.get_pos())
            if x != -1 and y != -1:
                if player_turn % 2 == 1:
                    tic_tac_toe_grid[y][x] = 1
                    player_turn += 1
                else:
                    tic_tac_toe_grid[y][x] = 2
                    player_turn += 1
                

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    draw_grid(screen)
    ui_manager.draw_ui(screen)

    pygame.display.flip()
    pygame.display.update()
