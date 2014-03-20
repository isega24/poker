from baraja import *

from variables import *

class Mano:
	def __init__(self,lista_de_cartas):
		self.mano = lista_de_cartas

	def muestra_longitud(self):
		return len(self.mano)

	def muestra_carta(self,indice):
		return self.mano[indice]

	def muestra_mano(self):
		return self.mano

	def recive_carta(self,carta):
		if len(self.mano) < 7:
			self.mano.append(carta)

	def descarta(self,indice):
		if len(self.mano)> indice and indice >= 0:
			self.mano.remove(self.mano[indice])
