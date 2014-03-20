from variables import *

import random


class Carta:
	def __init__(self, valor, palo):
		self.valor = valor
		self.palo = palo
		if valor == "As":
			self._puntuacion = 12
		elif valor == "K":
			self._puntuacion = 11
		elif valor == "Q":
			self._puntuacion = 10
		elif valor == "J":
			self._puntuacion = 9
		else:
			self._puntuacion = int(valor) - 2

	def info(self):
		return [self.valor,self.palo]

	def puntuacion(self):
		return self._puntuacion





class Baraja:
	def __init__(self):
		
		self.baraja = []
		for palo in palos:
			for valor in valores:
				una_carta = Carta(valor,palo)
				self.baraja.append(una_carta)

		self._usadas = 0

	def reparte(self):
		indice_carta = random.randint(0,N_CARTAS - self._usadas- 1)
		una_carta = self.baraja[indice_carta]
		if self._usadas < N_CARTAS:
			self._usadas = self._usadas + 1
			del self.baraja[indice_carta]
		return una_carta

	def usadas(self):

		return self._usadas

	def muestra_baraja(self):
		return self.baraja
	def elimina(self, carta):

		for valor in range(len(valores)):
			for palo in range(len(palos)):
				if carta.info()[0] == valor and carta.info()[1]==palo:
					self.baraja.remove(self.baraja[valor][palo])
