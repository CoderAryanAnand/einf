# Pygame Cheat Sheet: MVC, Pygame-GUI, and Sprites

This cheat sheet is based on the examples found in your workspace (e.g., `asteroids.py`, `tictactoe.py`, `probeprüfung4.py`).

## 1. MVC (Model-View-Controller) Pattern

In Pygame, MVC helps organize your code by separating data, display, and logic.

*   **Model**: The data and state of your game (variables, lists, sprite groups).
*   **View**: How things look on the screen (drawing functions, rendering sprites/UI).
*   **Controller**: Handling user input and updating the model (event loop, game logic).

### Example Structure (based on `tictactoe.py`)

```python
# --- MODEL (Data) ---
# The state of the game board
board_data = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
current_player = 1

# --- VIEW (Display) ---
def draw_board(screen):
    screen.fill((0, 0, 0)) # Clear screen
    # Draw grid lines
    # ... (drawing code) ...
    # Draw X and O based on board_data
    for r in range(3):
        for c in range(3):
            if board_data[r][c] == 1:
                pass # Draw X
            elif board_data[r][c] == 2:
                pass # Draw O

# --- CONTROLLER (Logic & Input) ---
while is_running:
    # 1. Handle Events (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Update Model based on Input
            x, y = get_board_coordinates(pygame.mouse.get_pos())
            board_data[y][x] = current_player
    
    # 2. Update Game State (Logic)
    # (e.g., check for win condition)

    # 3. Render (View)
    draw_board(screen)
    pygame.display.flip()
```

## 2. Pygame GUI (`pygame_gui`)

Used for creating buttons, menus, and text boxes. Requires `pygame_gui` library.

### Basic Setup
```python
import pygame
import pygame_gui

# 1. Initialize Manager
ui_manager = pygame_gui.UIManager((800, 600))

# 2. Create Elements (usually before the main loop)
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 130), (130, 20)),
    text='Click Me',
    manager=ui_manager
)

text_box = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((0, 10), (600, 200)),
    html_text="Hello World",
    manager=ui_manager
)

# 3. Main Loop Integration
clock = pygame.time.Clock()
while is_running:
    time_delta = clock.tick(60) / 1000.0 # Time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        # Pass events to UI Manager
        ui_manager.process_events(event)

        # Handle UI Events (e.g., button click)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                print("Button Pressed!")

    # Update UI Manager
    ui_manager.update(time_delta)

    # Draw UI
    screen.fill((0,0,0))
    ui_manager.draw_ui(screen)
    pygame.display.flip()
```

### Common Elements
*   **UILabel**: Simple text label.
*   **UIButton**: Clickable button.
*   **UITextBox**: Text area (supports HTML).
*   **UIDropDownMenu**: Dropdown selection.

## 3. Pygame Sprites (`pygame.sprite`)

Sprites are objects that can move, animate, and interact. They are managed in Groups.

### Creating a Sprite Class
Inherit from `pygame.sprite.Sprite`.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__() 
        # OR: pygame.sprite.Sprite.__init__(self)

        # 1. Image (Visual)
        self.image = pygame.image.load("img/player.png").convert()
        self.image.set_colorkey((0, 0, 0)) # Make black transparent
        # OR create a simple surface:
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 0, 0))

        # 2. Rect (Position & Hitbox)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400 # Initial X position
        self.rect.bottom = 580  # Initial Y position
        self.speedx = 0

    def update(self):
        # Logic to run every frame (movement, animation) (Hold button)
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
            
        self.rect.x += self.speedx

        # Boundary checks
        if self.rect.right > 800:
            self.rect.right = 800
```

### Using Sprites in Main Loop

```python
# 1. Create Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# 2. Create Instances and Add to Groups
player = Player()
all_sprites.add(player)

enemy = Enemy() # Assuming Enemy class exists
all_sprites.add(enemy)
enemies.add(enemy)

# 3. Main Loop
while is_running:
    # ... event handling ...

    # Update all sprites
    all_sprites.update()

    # Collision Detection
    # Check if player hits any enemy (True = kill enemy)
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False
        print("Game Over!")

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen) # Draws all sprites in the group
    pygame.display.flip()
```

### Key Methods
*   `sprite.kill()`: Removes the sprite from all groups.
*   `group.add(sprite)`: Adds a sprite to a group.
*   `group.update()`: Calls the `update()` method of every sprite in the group.
*   `group.draw(surface)`: Draws the `image` of every sprite at its `rect` position.
