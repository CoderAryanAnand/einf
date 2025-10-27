
def euclid_algo(a, b):
    if b == 0:
        return a
    return euclid_algo(b, a % b)

class Bruch:
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner

    def multiplizieren(self, anderer_bruch):
        neuer_zaehler = self.zaehler * anderer_bruch.zaehler
        neuer_nenner = self.nenner * anderer_bruch.nenner
        return Bruch(neuer_zaehler, neuer_nenner)
    
    def dividieren(self, anderer_bruch):
        neuer_zaehler = self.zaehler * anderer_bruch.nenner
        neuer_nenner = self.nenner * anderer_bruch.zaehler
        return Bruch(neuer_zaehler, neuer_nenner)
    
    def addieren(self, anderer_bruch):
        neuer_zaehler = (self.zaehler * anderer_bruch.nenner) + (anderer_bruch.zaehler * self.nenner)
        neuer_nenner = self.nenner * anderer_bruch.nenner
        return Bruch(neuer_zaehler, neuer_nenner)
    
    def subtrahieren(self, anderer_bruch):
        neuer_zaehler = (self.zaehler * anderer_bruch.nenner) - (anderer_bruch.zaehler * self.nenner)
        neuer_nenner = self.nenner * anderer_bruch.nenner
        return Bruch(neuer_zaehler, neuer_nenner)
    
    def kuerzen(self):
        divisor = euclid_algo(self.zaehler, self.nenner)
        self.zaehler //= divisor
        self.nenner //= divisor
        return self

    def __str__(self):
        return f"{self.zaehler}\n- \n{self.nenner}"
    
bruch1 = Bruch(3, 4)
bruch2 = Bruch(2, 5)
bruch3 = bruch1.multiplizieren(bruch2)
bruch4 = bruch1.dividieren(bruch2)
print(bruch3)
print(bruch4)

bruch5 = Bruch(6, 8)
print(bruch5.kuerzen())