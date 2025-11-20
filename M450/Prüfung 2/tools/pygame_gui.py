import pygame
import pygame_gui

# --- MODEL (Goal 21: Logic/Data) ---
# Stores the application state and logic. Does NOT handle drawing (View).
class GameModel:
    def __init__(self):
        self.message_data = "Initial Message"
        self.click_count = 0

    def update_message(self, new_text):
        """Updates the internal data based on a user action."""
        self.message_data = new_text
        print(f"MODEL updated: New message is '{self.message_data}'")

    def increment_count(self):
        self.click_count += 1
        return self.click_count

    def get_message(self):
        return self.message_data

# --- VIEW/CONTROLLER (Goal 21: Presentation/Logic Handling) ---
# Pygame and pygame_gui handle both view (drawing) and controller (input handling).

pygame.init()

pygame.display.set_caption('GUI MVC Demo')
WINDOW_SIZE = (800, 600)
window_surface = pygame.display.set_mode(WINDOW_SIZE)

# Goal 20: Implement a GUI with pygame_gui
manager = pygame_gui.UIManager(WINDOW_SIZE, 'themes/data/default_theme.json')
clock = pygame.time.Clock()
model = GameModel()

# Goal 19: Select suitable GUI elements (Button and Text Entry)
# Button for a given user interaction (e.g., "submit")
hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 50, 100, 50)),
    text='Click Me',
    manager=manager
)

# Text Entry for user interaction (e.g., inputting text)
text_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 150, 400, 50)),
    manager=manager,
    initial_text=model.get_message()
)

# Text Label to display model state
message_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 250, 400, 50)),
    text=f"Model State: {model.get_message()}",
    manager=manager
)

is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Controller: Handle UI events
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    # Controller logic: Call the Model to update data
                    count = model.increment_count()
                    
                    # Update the View (Label) with the new Model data
                    message_label.set_text(f"Button Clicked: {count} times!")

            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == text_input:
                    # Controller logic: Get text from View, call Model to update data
                    new_text = text_input.get_text()
                    model.update_message(new_text)

                    # Update the View (Label) with the new Model data
                    message_label.set_text(f"Model State: {model.get_message()}")


        manager.process_events(event)

    # VIEW: Update and Draw
    manager.update(time_delta)
    window_surface.fill(pygame.Color('#000000')) # Black background
    manager.draw_ui(window_surface)
    pygame.display.update()

pygame.quit()