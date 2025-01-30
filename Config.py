class Config:
	def __init__(self):
		self.langage = ""

		self.update_config()

	def update_config(self):
		with open("config.txt") as f:
			lignes = f.readlines()

		self.langage = lignes[0]

	def getLangage(self):
		return self.langage

	def setLangage(self, nouveau_langage):
		self.langage = nouveau_langage