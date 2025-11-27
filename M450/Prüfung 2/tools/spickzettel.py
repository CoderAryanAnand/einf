# ============================================================
# ULTIMATIVER SPICKZETTEL – OOP + pygame + pygame_gui
# Alles hier ist nur als Vorlage / Muster gedacht.
# Du kopierst dir im Notfall einzelne Teile in deine Pruefung.
# ============================================================


# ============================================================
# 1) OOP-BASIS: KLASSEN, ATTRIBUTE, METHODEN, __str__
# ============================================================

# Merksatz:
# - Dinge, die sich zwischen Objekten unterscheiden -> Parameter im __init__
# - Dinge, die immer gleich starten             -> fix im __init__ setzen
# - self.irgendwas = ...  erzeugt ein Attribut am Objekt


class SmartGeraet:
    def __init__(self, name, leistung_watt):
        # Parameter, weil jedes Geraet anders ist
        self._name = name
        self._leistung_watt = leistung_watt

        # Standardwerte, weil alles gleich startet
        self._betriebsstunden = 0
        self._zustand = "standby"

    def starte(self):
        self._zustand = "aktiv"
        return "System wird gestartet."

    def status(self):
        # Beispiel: "Laptop aktiv"
        return f"{self._name} {self._zustand}"

    def energieverbrauch(self):
        # Verbrauch = Leistung * Stunden
        verbrauch = self._leistung_watt * self._betriebsstunden
        return verbrauch  # oder f"{verbrauch} Wh"


geraet = SmartGeraet("Laptop", 65)
print(geraet.starte())
print(geraet.status())
print(geraet.energieverbrauch())


# ============================================================
# 2) __str__ UND DICTIONARY MIT OBJEKTEN (Monster / Robot / Autos)
# ============================================================

# Muster fuer viele Aufgaben: eine "Datenklasse" (Monster, Robot, Auto...),
# die Listen und Dicts als Attribute hat und ein schoenes __str__.

class Monster:
    def __init__(self, name, x, y, freunde, werte):
        self.name = name
        self.position = (x, y)    # Tupel (x, y)
        self.freunde = freunde    # Liste von Strings
        self.werte = werte        # Dict, z. B. {"Energie": 100, ...}

    def __str__(self):
        # join fuer Liste, Dict kann direkt ausgegeben werden
        return (
            f"Monster: {self.name}\n"
            f"Position: {self.position}\n"
            f"Freunde: {', '.join(self.freunde)}\n"
            f"Werte: {self.werte}"
        )


def monster_datenbank():
    m1 = Monster(
        "Hydra",
        100, 150,
        ["Nessie", "Bunyip"],
        {"Energie": 100, "Schild": 50, "Angriff": 20}
    )
    m2 = Monster(
        "Drache",
        300, 200,
        ["Hydra"],
        {"Energie": 150, "Schild": 30, "Angriff": 40}
    )

    # Dictionary mit Levelnamen -> Objekt
    monster_dict = {
        "Level 1": m1,
        "Level 2": m2
    }

    # items() liefert (key, value) Paare
    for level, monster in monster_dict.items():
        print(level)
        print(monster)      # ruft __str__ auf
        print("-" * 30)


# ============================================================
# 3) ANDERES BEISPIEL: AUTOS-GARAGE
# ============================================================

class Auto:
    def __init__(self, marke, modell, baujahr, km_stand, services, werte):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.km_stand = km_stand
        self.services = services      # Liste
        self.werte = werte            # Dict

    def __str__(self):
        return (
            f"Marke: {self.marke}\n"
            f"Modell: {self.modell}\n"
            f"Baujahr: {self.baujahr}\n"
            f"KM Stand: {self.km_stand}\n"
            f"Services: {', '.join(self.services)}\n"
            f"Werte: {self.werte}"
        )


def garage():
    car1 = Auto(
        "BMW",
        "M5",
        2021,
        2,
        ["Oelwechsel", "Reifen", "Bremsen"],
        {"Leistung": "535 PS", "Tank": "70 L", "Verbrauch": "5.0 L/100 km"}
    )
    car2 = Auto(
        "BMW",
        "M4",
        2023,
        222,
        ["Oelwechsel", "Reifen", "Bremsen"],
        {"Leistung": "480 PS", "Tank": "60 L", "Verbrauch": "9.7 L/100 km"}
    )

    garage_dict = {
        "Auto 1": car1,
        "Auto 2": car2
    }

    for key, value in garage_dict.items():
        print(key)
        print(value)
        print("-" * 40)


# ============================================================
# 4) PYGAME-GRUNDGERUeST (OHNE pygame_gui)
# ============================================================

# Merksatz:
# - pygame.init()
# - screen = display.set_mode(...)
# - while running:
#       events holen
#       zeichnen
#       display.flip()
#       clock.tick(60)

if False:  # nur Vorlage, nicht automatisch ausfuehren
    import pygame
    import random

    class Box:
        def __init__(self, x, y, width, height):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = pygame.Color(255, 255, 255)

        def change_color(self):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.color = pygame.Color(r, g, b)

    class BoxView:
        def __init__(self, box):
            self.box = box

        def draw(self, surface):
            pygame.draw.rect(surface, self.box.color, self.box.rect)

    def simple_main():
        pygame.init()
        screen_width, screen_height = 500, 500
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Simple Box")

        clock = pygame.time.Clock()

        box = Box(200, 200, 100, 100)
        box_view = BoxView(box)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        box.change_color()

            screen.fill((0, 0, 0))
            box_view.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


# ============================================================
# 5) PYGAME + pygame_gui: MVC-BOX MIT BUTTON
# ============================================================

# Merksatz:
# - Model: haelt Daten und Logik (Box)
# - View: zeichnet (BoxView)
# - Controller / main: Events (Button), ruft Model-Methoden auf

if False:  # Vorlage
    import pygame
    import pygame_gui
    import random

    class Box:
        def __init__(self, x, y, width, height):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = pygame.Color(0, 0, 0)

        def change_color(self):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.color = pygame.Color(r, g, b)

    class BoxView:
        def __init__(self, box):
            self.box = box

        def zeichne(self, surface):
            pygame.draw.rect(surface, self.box.color, self.box.rect)

    def mvc_main():
        pygame.init()
        screen_width, screen_height = 500, 500
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("MVC Box")

        clock = pygame.time.Clock()

        manager = pygame_gui.UIManager((screen_width, screen_height))

        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(10, 10, 120, 40),
            text="Farbe aendern",
            manager=manager
        )

        box = Box(200, 150, 200, 150)
        box_view = BoxView(box)

        running = True
        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # wichtig: Events an manager geben
                manager.process_events(event)

                # Button-Click pruefen (innerhalb der Schleife!)
                if (event.type == pygame.USEREVENT
                        and event.user_type == pygame_gui.UI_BUTTON_PRESSED
                        and event.ui_element == button):
                    box.change_color()

            manager.update(time_delta)

            screen.fill((30, 30, 30))
            box_view.zeichne(screen)
            manager.draw_ui(screen)
            pygame.display.flip()

        pygame.quit()


# ============================================================
# 6) SPRITE-VORLAGE (Fisch / Mine / allgemein)
# ============================================================

# Merksatz fuer jede Sprite-Klasse:
# class Ding(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = ...
#         self.rect = self.image.get_rect()
#         self.rect.x / self.rect.y = Startposition
#         self.speed = ...
#
#     def update(self):
#         Bewegung ueber rect.x / rect.y


if False:  # Vorlage
    import pygame
    import random

    WIDTH, HEIGHT = 600, 600

    class Fish(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            # Entweder mit Bild:
            # self.image = pygame.image.load("fish.png").convert_alpha()
            # self.image = pygame.transform.scale(self.image, (80, 50))

            # oder einfache Flaeche:
            self.image = pygame.Surface((40, 20))
            self.image.fill((255, 120, 0))

            self.rect = self.image.get_rect()
            self.rect.x = random.randint(-300, -50)
            self.rect.y = random.randint(50, HEIGHT - 150)
            self.speed = random.randint(1, 4)

        def update(self):
            self.rect.x += self.speed
            if self.rect.x > WIDTH + 50:
                self.rect.x = random.randint(-300, -50)
                self.rect.y = random.randint(50, HEIGHT - 150)
                self.speed = random.randint(1, 4)

    class Mine(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            # self.image = pygame.image.load("mine.png").convert_alpha()
            # self.image = pygame.transform.scale(self.image, (40, 40))
            self.image = pygame.Surface((30, 30))
            self.image.fill((100, 100, 100))

            self.rect = self.image.get_rect()
            self.rect.x = random.randint(50, WIDTH - 50)
            self.rect.y = random.randint(-300, -50)
            self.speed = random.randint(1, 3)

        def update(self):
            self.rect.y += self.speed
            if self.rect.y > HEIGHT + 50:
                self.rect.y = random.randint(-300, -50)
                self.rect.x = random.randint(50, WIDTH - 50)
                self.speed = random.randint(1, 3)


# ============================================================
# 7) UNTERWASSER-WELT (Fische, Minen, Blasen, U-Boot)
# ============================================================

if False:  # vollstaendige Vorlage in einfach
    import pygame
    import random

    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("U-Boot Spiel")
    clock = pygame.time.Clock()

    class Fish(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((40, 20))
            self.image.fill((255, 120, 0))
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(-300, -50)
            self.rect.y = random.randint(50, HEIGHT - 150)
            self.speed = random.randint(1, 4)

        def update(self):
            self.rect.x += self.speed
            if self.rect.x > WIDTH + 50:
                self.rect.x = random.randint(-300, -50)
                self.rect.y = random.randint(50, HEIGHT - 150)
                self.speed = random.randint(1, 4)

    class Mine(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((30, 30))
            self.image.fill((100, 100, 100))
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(50, WIDTH - 50)
            self.rect.y = random.randint(-300, -50)
            self.speed = random.randint(1, 3)

        def update(self):
            self.rect.y += self.speed
            if self.rect.y > HEIGHT + 50:
                self.rect.y = random.randint(-300, -50)
                self.rect.x = random.randint(50, WIDTH - 50)
                self.speed = random.randint(1, 3)

    # Blasen als einfache Kreise
    bubbles = []
    for _ in range(40):
        bubbles.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

    # U-Boot als Rechteck
    sub_rect = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 120, 80, 40)

    fish_group = pygame.sprite.Group()
    mine_group = pygame.sprite.Group()

    for _ in range(6):
        fish_group.add(Fish())
    for _ in range(4):
        mine_group.add(Mine())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Hintergrund
        screen.fill((0, 70, 120))

        # Blasen
        for b in bubbles:
            b[1] -= 1
            if b[1] < -10:
                b[1] = HEIGHT + 10
                b[0] = random.randint(0, WIDTH)
            pygame.draw.circle(screen, (140, 190, 255), b, 5)

        # Sprites
        fish_group.update()
        mine_group.update()
        fish_group.draw(screen)
        mine_group.draw(screen)

        # U-Boot
        pygame.draw.rect(screen, (255, 220, 0), sub_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# ============================================================
# SPICKZETTEL – COLLISIONS IN PYGAME
# ============================================================
# Hier sind die haeufigsten Muster, wie du Kollisionen pruefst.
# Du kannst dir einzelne Teile rausziehen und in deine Programme einbauen.
# ============================================================

import pygame

# ------------------------------------------------------------
# 1) Kollision mit Rects (ohne Sprites)
# ------------------------------------------------------------
# Merksatz:
#   rect1.colliderect(rect2)  -> True, wenn sich die Rechtecke schneiden

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(120, 120, 60, 60)

if rect1.colliderect(rect2):
    print("Kollision zwischen rect1 und rect2!")


# ------------------------------------------------------------
# 2) Kollision: Sprite vs. Rect
# ------------------------------------------------------------
# Wenn du Sprites hast, deren rect du pruefen willst:

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(200, 200))


player = Player()
wand_rect = pygame.Rect(250, 180, 50, 100)

if player.rect.colliderect(wand_rect):
    print("Player kollidiert mit Wand!")


# ------------------------------------------------------------
# 3) Kollision: Ein Sprite vs. Sprite-Gruppe
# ------------------------------------------------------------
# Merksatz:
#   pygame.sprite.spritecollide(sprite, gruppe, dokill)
#
# - sprite    : das eine Sprite, das du pruefen willst (z. B. Player)
# - gruppe    : Gruppe von Sprites, z. B. Gegner oder Minen
# - dokill    : True -> getroffene Sprites werden aus der Gruppe entfernt

class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))


player = Player()
mine_group = pygame.sprite.Group()
mine_group.add(Mine(220, 200))
mine_group.add(Mine(400, 300))

# Kollisionen zwischen player und allen Minen suchen:
treffer_liste = pygame.sprite.spritecollide(player, mine_group, False)

if treffer_liste:
    print("Player trifft mindestens eine Mine!")
    # treffer_liste ist eine Liste von Mine-Objekten
    for mine in treffer_liste:
        print("Getroffene Mine:", mine)


# Beispiel mit Entfernen:
treffer_liste = pygame.sprite.spritecollide(player, mine_group, True)
# True -> getroffene Minen werden automatisch aus mine_group entfernt


# ------------------------------------------------------------
# 4) Kollision: Gruppe vs. Gruppe (z. B. Schuesse vs. Gegner)
# ------------------------------------------------------------
# Merksatz:
#   pygame.sprite.groupcollide(gruppe1, gruppe2, dokill1, dokill2)
#
# Rueckgabe:
#   dict: {spriteAusGruppe1: [getroffeneSpritesAusGruppe2, ...], ...}

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(x, y))


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

bullet_group.add(Bullet(200, 200))
enemy_group.add(Enemy(200, 200))
enemy_group.add(Enemy(300, 300))

# Kollisionen zwischen allen Bullets und allen Enemies:
treffer_dict = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
# True, True -> getroffene Bullets und Enemies werden aus den Gruppen entfernt

if treffer_dict:
    print("Es gab Kollisionen zwischen Bullets und Enemies!")
    # treffer_dict: {BulletObjekt: [Enemy1, Enemy2, ...], ...}
    for bullet, enemies in treffer_dict.items():
        print("Bullet", bullet, "hat", len(enemies), "Enemies getroffen.")


# ------------------------------------------------------------
# 5) Typischer Einsatz in einem Game-Loop (Beispiel)
# ------------------------------------------------------------
# Muster fuer eine simple Game-Loop mit Kollision zwischen Player und Minen:

if False:  # nur Vorlage, damit es nicht automatisch laeuft
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)  # praktische 1er-Gruppe

    mine_group = pygame.sprite.Group()
    for i in range(5):
        mine_group.add(Mine(100 + i * 80, 300))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Hier wuerdest du Player bewegen etc.

        # Kollision Player vs. Mine-Gruppe:
        hits = pygame.sprite.spritecollide(player, mine_group, False)
        if hits:
            print("BOOM! Player hat eine Mine beruehrt.")

        screen.fill((30, 30, 30))
        player_group.draw(screen)
        mine_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
# ============================================================
# ============================================================
# ENDE DES SPICKZETTELS
# - Du musst NICHT alles auswendig koennen.
# - Wichtig sind die Muster:
#   * OOP: __init__, Attribute, Methoden, __str__, Dict + for key, value
#   * pygame: Grundgeruest, Event-Loop, rect, draw, clock.tick(60)
#   * pygame_gui: manager, UIButton, USEREVENT, UI_BUTTON_PRESSED
#   * Sprites: Vererbung, super().__init__(), image, rect, update
# ============================================================

