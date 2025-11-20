# --- SCHUMMELZETTEL 3: MVC & GUI (Based on 3.py & tictactoe.py) ---
import pygame
import pygame_gui
import random

# --- 1. MODEL (Die Logik/Daten - Goal 21) ---
# Hält nur Daten, weiß NICHTS von Pygame oder GUI
class Model:
    def __init__(self):
        self.color = (255, 0, 0) # Startfarbe
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Daten für Grid (TicTacToe)

    def change_color_random(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def set_grid_value(self, row, col, value):
        self.grid[row][col] = value

# --- 2. VIEW (Die Darstellung - Goal 21) ---
# Bekommt das Model, um es zu zeichnen
class View:
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        # Zeichne Box (3.py Style)
        pygame.draw.rect(surface, self.model.color, pygame.Rect(100, 100, 200, 200))
        
        # Zeichne Grid Linien (TicTacToe Logic simplified)
        # ... (pygame.draw.line calls...)

# --- MAIN / CONTROLLER (Steuerung - Goal 19, 20) ---
pygame.init()
screen = pygame.display.set_mode((600, 600))
ui_manager = pygame_gui.UIManager((600, 600))
clock = pygame.time.Clock()

# Instanzen erstellen
my_model = Model()
my_view = View(my_model)

# GUI Elemente erstellen (Goal 19)
btn_change = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 350), (200, 50)),
    text='Farbe ändern',
    manager=ui_manager
)

is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # --- GUI EVENTS (Goal 20) ---
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == btn_change:
                # Controller ändert Model
                my_model.change_color_random()

        # --- MOUSE EVENTS (TicTacToe Logic) ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Logik um Mausposition in Grid umzuwandeln (aus tictactoe.py)
            # x, y = mouse_pos... check boundaries...
            pass 

        ui_manager.process_events(event)

    # --- DRAWING ---
    ui_manager.update(time_delta)
    
    screen.fill((0, 0, 0))
    
    # 1. View zeichnen (Spielinhalt)
    my_view.draw(screen)
    
    # 2. UI zeichnen (Buttons/Labels)
    ui_manager.draw_ui(screen)

    pygame.display.update()