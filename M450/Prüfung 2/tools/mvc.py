#mvc = model, view, controller
#model = daten, logik
#view = darstellung
#controller = benutzerinteraktion, steuerung
class Model:
    def __init__(self):
        self.count = 0
        self._observers = []

    def inc(self):
        self.count += 1
        self._notify()

    def register(self, obs):
        self._observers.append(obs)

    def _notify(self):
        for o in self._observers:
            o.update(self)


class View:
    def update(self, model):
        print(f"Aktueller Wert: {model.count}")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        model.register(view)

    def run(self):
        print("Enter zum Erhöhen, q + Enter zum Beenden")
        while True:
            cmd = input()
            if cmd.lower() == "q":
                break
            self.model.inc()


if __name__ == "__main__":
    m = Model()
    v = View()
    c = Controller(m, v)
    c.run()