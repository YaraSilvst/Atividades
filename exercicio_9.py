class Carro():


	def __init__(self, capacidade, consumo):
		self.capacidade = capacidade
		self.cosnumo = consumo
		self.litros = 0 


	def mover(km):
		gasto = km / self.consumo

		if self.litros >= gasto:
			self.litros = self.litros - gasto

		else:
			self.litros = 0


	def gasolina():
		return self.litros

	def abastecer(self, litros):
		if (self.litros + litros) >= self.capacidade:
			self.litros = self.capacidade
		elif (self.litros + litros) < self.capacidade:
		      self.litros = self.litros + litros
		else:
			print("O tanque está cheio!")



