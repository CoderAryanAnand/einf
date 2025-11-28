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

log_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (5, 500), (130, 40)), text="Player 1 turn", manager=ui_manager)

positions_of_grid_cells = [[(175, 25), (310, 25), (440, 25)],
                           [(175, 160), (310, 160), (440, 160)],
                           [(175, 290), (310, 290), (440, 290)]]

class TicTacToe:
    def __init__(self):
        self.grid = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1
        self.current_move = 0

    def check_winner(self):
        g = self.grid
        for i in range(3):
            if g[i][0] == g[i][1] == g[i][2] != 0:
                return g[i][0]
            if g[0][i] == g[1][i] == g[2][i] != 0:
                return g[0][i]
        if g[0][0] == g[1][1] == g[2][2] != 0:
            return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != 0:
            return g[0][2]
        return 0

    def is_finished(self):
        if self.check_winner() != 0:
            return True
        for row in self.grid:
            if 0 in row:
                return False
        return True

    def play(self, x, y):
        # x = column, y = row
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        if self.grid[y][x] != 0:
            return False
        self.grid[y][x] = self.current_player
        self.current_move += 1
        self.current_player = 2 if self.current_player == 1 else 1
        return True

    def get_field(self, x, y):
        return self.grid[y][x]

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
            if game.grid[y][x] == 1:
                x_img = pygame.image.load('M450/7011 - tictactoe/img/x.png')
                x_img = pygame.transform.scale(x_img, (cell_size - 20, cell_size - 20))
                position = positions_of_grid_cells[y][x]
                screen.blit(x_img, position)
            elif game.grid[y][x] == 2:
                o_img = pygame.image.load('M450/7011 - tictactoe/img/o.png')
                o_img = pygame.transform.scale(o_img, (cell_size - 20, cell_size - 20))
                position = positions_of_grid_cells[y][x]
                screen.blit(o_img, position)

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


game = TicTacToe()

is_running = True

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
                moved = game.play(x, y)
                if moved:
                    winner = game.check_winner()
                    if winner != 0:
                        log_text.set_text(f"Player {winner} wins!")
                    elif game.is_finished():
                        log_text.set_text("Draw!")
                    else:
                        log_text.set_text(f"Player {game.current_player} turn")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == restart_button:
                game = TicTacToe()
                log_text.set_text("Player 1 turn")
                

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    draw_grid(screen)
    ui_manager.draw_ui(screen)

    pygame.display.flip()
    pygame.display.update()
