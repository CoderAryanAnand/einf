

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        return f"{self.name} says Meow!"
    
    def fressen(self):
        return f"{self.name} is eating."
    


bob_the_cat = Cat("Bob", 3, "gray")
print(bob_the_cat.meow())
print(bob_the_cat.fressen())