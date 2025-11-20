
class SmartGeraet:
	def __init__(self, name, leistung_watt):
		self.name = name
		self.leistung_watt = leistung_watt
		self.betriebsstunden = 0
		self.zustand = "standby"
	
	def starte(self):
		print("System wird gestart")
	def status(self):
		return self.zustand
	def energieverbrauch(self):
		return self.leistung_watt * self.betriebsstunden
	
new_geraet = SmartGeraet("Kaffeemaschine", 800)

new_geraet.starte()
print("Zustand:", new_geraet.status())
print("Energieverbrauch:", new_geraet.energieverbrauch(), "Wh")