import pygame
import pygame_gui
import json
import os
import time

FPS = 60

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
UI_LEFT_PANEL_WIDTH = 75
UI_LOG_TEXT_BOX_HEIGHT = 300
GRID_H_PADDING = 100
GRID_V_PADDING = 25
GRID_SIZE = 400
PARTICIPANTS = ("Human", "AI Random")

HIGHSCORE_FILE = "M450/7011 - tictactoe/highscores.json"

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

# highscore display
highscore_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (5, 700), (130, 80)), text="Highscores:\n", manager=ui_manager)

positions_of_grid_cells = [[(185, 35), (320, 35), (450, 35)],
                           [(185, 170), (320, 170), (450, 170)],
                           [(185, 300), (320, 300), (450, 300)]]

# utility highscore functions
def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # ensure keys are strings (in case file was malformed)
                return {str(k): v for k, v in data.items()}
            except Exception:
                return {}
    return {}

def save_highscores(hs):
    # JSON requires string keys — coerce them
    hs_str_keys = {str(k): v for k, v in hs.items()}
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(hs_str_keys, f, ensure_ascii=False, indent=2)

def update_highscores(name, points):
    # normalize name to a plain string (handle tuple/list from UI components)
    if isinstance(name, (tuple, list)):
        name_key = str(name[0]) if len(name) > 0 else "Unknown"
    else:
        name_key = str(name)
    hs = load_highscores()
    hs[name_key] = hs.get(name_key, 0) + points
    save_highscores(hs)
    refresh_highscore_label()

def refresh_highscore_label():
    hs = load_highscores()
    items = sorted(hs.items(), key=lambda kv: kv[1], reverse=True)[:5]
    text = "Highscores:\n"
    for i, (n, p) in enumerate(items, 1):
        text += f"{i}. {n}: {p}\n"
    highscore_label.set_text(text)

# initial refresh
refresh_highscore_label()

class TicTacToe:
    def __init__(self):
        self.grid = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1
        self.current_move = 0
        self.game_over = False
        self.winner_combo = None  # list of (y,x) tuples when someone wins

    def check_winner(self):
        g = self.grid
        # rows
        for i in range(3):
            if g[i][0] == g[i][1] == g[i][2] != 0:
                self.winner_combo = [(i, 0), (i, 1), (i, 2)]
                self.game_over = True
                return g[i][0]
        # cols
        for i in range(3):
            if g[0][i] == g[1][i] == g[2][i] != 0:
                self.winner_combo = [(0, i), (1, i), (2, i)]
                self.game_over = True
                return g[0][i]
        # diag
        if g[0][0] == g[1][1] == g[2][2] != 0:
            self.winner_combo = [(0, 0), (1, 1), (2, 2)]
            self.game_over = True
            return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != 0:
            self.winner_combo = [(0, 2), (1, 1), (2, 0)]
            self.game_over = True
            return g[0][2]
        return 0

    def is_finished(self):
        if self.check_winner() != 0:
            return True
        for row in self.grid:
            if 0 in row:
                return False
        self.game_over = True
        return True

    def play(self, x, y):
        # x = column, y = row
        if not self.game_over:
            if x < 0 or x > 2 or y < 0 or y > 2:
                return False
            if self.grid[y][x] != 0:
                return False
            self.grid[y][x] = self.current_player
            self.current_move += 1
            self.current_player = 2 if self.current_player == 1 else 1
            return True
        return False

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

def draw_winner_line(screen, combo):
    if not combo:
        return
    # draw line from center of first cell to center of last cell
    first = positions_of_grid_cells[combo[0][0]][combo[0][1]]
    last = positions_of_grid_cells[combo[2][0]][combo[2][1]]
    # these positions are top-left offsets for images; calculate centers
    cell_size = GRID_SIZE // 3
    fx = first[0] + (cell_size - 20)//2
    fy = first[1] + (cell_size - 20)//2
    lx = last[0] + (cell_size - 20)//2
    ly = last[1] + (cell_size - 20)//2
    pygame.draw.line(screen, pygame.Color('red'), (fx, fy), (lx, ly), 6)

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

# animate tokens flying out before restart
def eject_tokens_and_reset():
    # collect tokens with their starting centers and velocities
    cell_size = GRID_SIZE // 3
    tokens = []
    speed = 600  # pixels per second
    for y in range(3):
        for x in range(3):
            v = game.grid[y][x]
            if v != 0:
                pos = positions_of_grid_cells[y][x]
                cx = pos[0] + (cell_size - 20)//2
                cy = pos[1] + (cell_size - 20)//2
                # velocity away from center of board
                board_cx = GRID_H_PADDING + UI_LEFT_PANEL_WIDTH + GRID_SIZE/2
                board_cy = GRID_V_PADDING + GRID_SIZE/2
                dx = cx - board_cx
                dy = cy - board_cy
                dist = max((dx*dx + dy*dy)**0.5, 0.001)
                vx = (dx / dist) * speed
                vy = (dy / dist) * speed
                tokens.append({"x": cx, "y": cy, "vx": vx, "vy": vy, "val": v})
    # animate for ~0.6s or until all offscreen
    start = time.time()
    duration = 0.6
    while True:
        dt = clock.tick(FPS) / 1000.0
        screen.fill(pygame.Color('#000000'))
        # move tokens
        all_off = True
        for t in tokens:
            t["x"] += t["vx"] * dt
            t["y"] += t["vy"] * dt
            if -100 < t["x"] < SCREEN_WIDTH + 100 and -100 < t["y"] < SCREEN_HEIGHT + 100:
                all_off = False
            # draw token
            if t["val"] == 1:
                img = pygame.image.load('M450/7011 - tictactoe/img/x.png')
            else:
                img = pygame.image.load('M450/7011 - tictactoe/img/o.png')
            img = pygame.transform.scale(img, (cell_size - 20, cell_size - 20))
            # blit centered
            screen.blit(img, (t["x"] - (cell_size - 20)//2, t["y"] - (cell_size - 20)//2))
        ui_manager.update(0)
        ui_manager.draw_ui(screen)
        pygame.display.flip()
        if all_off or (time.time() - start) > duration:
            break
    # finally reset the game
    return TicTacToe()

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
                        # update highscores: winner gets 3 points
                        winner_name = part1.selected_option if winner == 1 else part2.selected_option
                        update_highscores(winner_name, 3)
                        log_text.set_text(f"Player {winner} ({winner_name}) wins!")
                    elif game.is_finished():
                        # draw: both get 1 point
                        update_highscores(part1.selected_option, 1)
                        update_highscores(part2.selected_option, 1)
                        log_text.set_text("Draw!")
                    else:
                        log_text.set_text(f"Player {game.current_player} turn")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == restart_button:
                # animate tokens flying out, then replace game
                game = eject_tokens_and_reset()
                log_text.set_text("Player 1 turn")
                

    ui_manager.update(time_delta)

    screen.fill(pygame.Color('#000000'))
    draw_grid(screen)
    # draw winning line if present
    if game.winner_combo:
        draw_winner_line(screen, game.winner_combo)
    ui_manager.draw_ui(screen)

    pygame.display.flip()
    pygame.display.update()
