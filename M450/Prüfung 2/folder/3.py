"""
Erstellen Sie einen Rechner für Multiplikation und Division mit GUI. 
Dabei sollen zwei Zahlen eingegeben, die Operation gewählt und die Berechnung ausgeführt werden können.

Verwenden Sie das MVC Prinzip.
"""

import pygame
import pygame_gui

class Result:
    def __init__(self, x, y, width, height, ui_manager):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = "0"
        self.ui_manager = ui_manager

    def mult(self, num1, num2):
        self.text = int(num1)*int(num2)

    def div(self, num1, num2):
        self.text = int(num1)/int(num2)

class ResultView:
    def __init__(self, box):
        self.box = box

    def zeichne(self, surface):
        pygame_gui.elements.UILabel(relative_rect=self.box.rect, text=self.box.text, manager=self.box.ui_manager)

def mvc_main():
    pygame.init()
    screen_width, screen_height = 600, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("MVC Box")

    clock = pygame.time.Clock()

    manager = pygame_gui.UIManager((screen_width, screen_height))

    mbutton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(10, 50, 120, 40),
        text="Multiply",
        manager=manager
    )

    dbutton = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(10, 10, 120, 40),
        text="divide",
        manager=manager
    )

    text1_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 150, 400, 50)),
    manager=manager
)

    text2_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 450, 400, 50)),
    manager=manager
)

    box = Result(200, 150, 200, 150, manager)
    box_view = ResultView(box)

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            manager.process_events(event)

            # Button-Click pruefen (innerhalb der Schleife!)
            if (event.type == pygame.USEREVENT
                    and event.user_type == pygame_gui.UI_BUTTON_PRESSED):
                if event.ui_element == mbutton:
                    box.mult(text1_input.text, text2_input.text)
                else:
                    box.div(text1_input.text, text2_input.text)

        manager.update(time_delta)

        screen.fill((30, 30, 30))
        box_view.zeichne(screen)
        manager.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()


mvc_main()