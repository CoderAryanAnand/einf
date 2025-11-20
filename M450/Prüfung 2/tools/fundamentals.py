# --------------------------
# 1. Variables (Goal 4)
# --------------------------
# Creating variables without external data (without Unterlagen)
game_title = "Pygame Adventure" # String variable
max_players = 4                # Integer variable
is_running = True              # Boolean variable
PI = 3.14159                   # Float variable

print(f"Game Title: {game_title}")
print(f"Max Players: {max_players}")

# --------------------------
# 2. Input and Output (Ein- und Ausgabe) (Goal 3)
# --------------------------
# Simple console I/O
print("\n--- Input/Output Demo ---")

# Output
print("Please enter your high score.")

# Input (Always returns a string, needs conversion for numbers)
try:
    user_input = input("Enter score: ")
    high_score = int(user_input)
    print(f"Thank you. Your score is recorded as: {high_score}")
except ValueError:
    print("Invalid input. Please enter a number.")
    high_score = 0


# --------------------------
# 3. One-Dimensional List (Goal 5)
# --------------------------
print("\n--- List Manipulation Demo (with Unterlagen) ---")

# Create a one-dimensional list
inventory = ["Sword", "Shield", "Potion", "Key"]
print(f"Original Inventory: {inventory}")

# Access and print an element (manipulieren)
print(f"First item (index 0): {inventory[0]}")

# Manipulate/Change an element
inventory[2] = "Super Potion"
print(f"Inventory after upgrade: {inventory}")

# Add a new element
inventory.append("Gold Coin")
print(f"Inventory after finding coin: {inventory}")

# Remove an element
inventory.remove("Shield")
print(f"Inventory after losing shield: {inventory}")


# Goal 8: Explain what a class is (the blueprint for Entity)
# Goal 14: Creating suitable classes for a problem (Entity is suitable for a game)
class Entity:
    """
    This is the blueprint (Class) for any game object 
    that moves and has health.
    """
    
    # Class-level attribute (shared by all instances)
    DEFAULT_SPEED = 5
    
    # Goal 13: Implement a meaningful constructor (the __init__ method)
    def __init__(self, name, health, x_pos, y_pos):
        """Initializes a new Entity object (The Constructor)."""
        # Goal 9: Attributes (Data/State)
        self.name = name          # String
        self.health = health      # Integer
        self.x = x_pos            # Position x
        self.y = y_pos            # Position y
        self.is_alive = True      # Boolean

    # Goal 10: Methods (Behavior)
    def take_damage(self, amount):
        """Reduces health and checks if the entity dies."""
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health remaining: {self.health}")
        if self.health <= 0:
            self.die()

    # Goal 11: Method calling another method of the same class
    def die(self):
        """Internal method called when health drops to 0 or below."""
        self.is_alive = False
        self.x = -1 # Move off screen
        print(f"*** {self.name} has been defeated! ***")
        
    def move(self, direction, distance):
        """Changes the entity's position."""
        if direction == 'up':
            self.y -= distance
        elif direction == 'down':
            self.y += distance
        # Calls the 'info' method (Goal 11)
        self.get_info() 

    def get_info(self):
        """Prints the current state of the object."""
        print(f"\n--- Entity State ---")
        print(f"Name: {self.name}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Is Alive: {self.is_alive}")
        
        
# --- Object Instantiation (Creating Instances) ---

# Create two Objects (Goal 8: What an object is)
player = Entity("Hero", 100, 50, 50)
enemy = Entity("Goblin", 30, 100, 100)

# Demonstrate Attributes (Goal 9)
print(f"The {player.name} starts at ({player.x}, {player.y}) with {player.health} HP.")
print(f"The Goblin's default speed is: {Entity.DEFAULT_SPEED}")

# Demonstrate Methods (Goal 10, 11)
player.move('right', 10) # Calls 'move', which calls 'get_info'

print("\n--- Combat Simulation ---")
player.take_damage(15)
enemy.take_damage(25)
enemy.take_damage(10) # This will cause the enemy to die (calls the die() method)

# Goal 12: Difference between Classes and Objects
print("\n--- Class vs Object Difference ---")
# 'Entity' is the Class (The template). 'player' and 'enemy' are Objects (The instances).
print(f"The 'player' variable is an object of type: {type(player).__name__}")
print(f"The 'Entity' type is the class blueprint: {Entity}")

# add a section explaining difference between list, tuples, sets and dictionaries
# --------------------------
# 4. Data Structures Overview (Goal 6)
print("\n--- Data Structures Overview ---")
# List: Ordered, mutable collection
my_list = [1, 2, 3, 4]
print(f"List: {my_list} (Type: {type(my_list).__name__})")
# Tuple: Ordered, immutable collection
my_tuple = (1, 2, 3, 4)
print(f"Tuple: {my_tuple} (Type: {type(my_tuple).__name__})")
# Set: Unordered, mutable collection of unique items
my_set = {1, 2, 3, 4}
print(f"Set: {my_set} (Type: {type(my_set).__name__})")
# Dictionary: Unordered, mutable collection of key-value pairs
my_dict = {'one': 1, 'two': 2, 'three': 3}
print(f"Dictionary: {my_dict} (Type: {type(my_dict).__name__})")