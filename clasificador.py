from baraja import *

from mano import *

from crupier import *

from variables import *

from impresor import *


class Clasificador:
	def __init__(self):
		pass

	def crea_matriz_cartas(self,mano):
		matriz = []
		for i in range(len(palos)):
		    matriz.append([])
		    for j in range(len(valores)):
		        matriz[i].append(0)

		for carta in mano.muestra_mano():

			indice_palo = palos.index(carta.info()[1])
			indice_valor = valores.index(carta.info()[0])
			matriz[indice_palo][indice_valor] = 1

		return matriz



	def transforma_a_mano(self,mano,mesa):
		lista_cartas = mano.muestra_mano()+mesa.muestra_mano()
		mano = Mano(lista_cartas)
		return mano

	def es_poker(self,matriz):
		valor = 0
		_es_poker = False
		el_poker_de = -1
		while valor < len(valores) and not _es_poker:
			n = 0
			for palo in range(len(palos)):
				if matriz[palo][valor] == 1:
					n = n +1
			if n == 4:
				_es_poker = True
				el_poker_de = valor
			valor = valor +1

		return [_es_poker,el_poker_de]
		

		

	def es_trio(self,matriz):
		valor = 0
		_es_trio = False
		el_trio_de = -1
		while valor < len(valores) and not _es_trio:
			n = 0
			for palo in range(len(palos)):
				if matriz[palo][valor] == 1:
					n = n +1
			if n == 3:
				_es_trio = True
				el_trio_de = valor
			valor = valor + 1

		return [_es_trio,el_trio_de]

	def es_pareja(self,matriz):
		valor = 0
		_es_pareja = False
		pareja_de = -1
		while valor < len(valores) and not _es_pareja:
			n = 0
			for palo in range(len(palos)):
				if matriz[palo][valor] == 1:
					n = n +1
			if n == 2:
				_es_pareja = True
				pareja_de = valor
			valor = valor +1

		return [_es_pareja,pareja_de]

	def es_color(self,matriz):
		palo = 0
		_es_color = False
		_color = -1
		while palo < len(palos) and not _es_color:
			n = 0
			for valor in range(len(valores)):
				if matriz[palo][valor] == 1:
					n = n +1
			if n >= 5:
				_es_color = True
				_color= palo
			palo = palo + 1
		return [_es_color,_color]

	def es_escalera(self,matriz):
		valor = 0
		_es_escalera = False
		contador = 0
		contador_maximo = 0
		carta_mas_alta = -1
		while valor < len(valores):
			hay_carta = False
			palo = 0
			while palo < len(palos) and not hay_carta:
				if matriz[palo][valor] == 1:
					hay_carta = True
				palo = palo + 1
			if hay_carta:
				contador = contador + 1
				if contador > contador_maximo:
					contador_maximo = contador
					carta_mas_alta = valor
			else:
				contador = 0
			valor = valor +1
		if contador == 4:
			for palo in range(len(palos)):
				if matriz[palo][0] == 1:
					contador_maximo = 5
					carta_mas_alta = 0

		_es_escalera = contador_maximo >= 5

		return [_es_escalera,carta_mas_alta]

	def es_doble_pareja(self,matriz):
		valor = 0
		n_parejas = 0
		primera_pareja = -1
		segunda_pareja = -1
		while valor < len(valores):
			n = 0
			for palo in range(len(palos)):
				if matriz[palo][valor] == 1:
					n = n +1
			if n == 2:
				n_parejas = n_parejas + 1
				if primera_pareja == -1:
					primera_pareja = valor
				else:
					segunda_pareja = valor

			valor = valor + 1
		if primera_pareja == 0:
			aux = primera_pareja
			primera_pareja = segunda_pareja
			segunda_pareja = aux
		if n_parejas >= 2:
			return [True,segunda_pareja,primera_pareja]

		else:
			return [False]

	def es_full(self,matriz):
		if self.es_pareja(matriz)[0] and self.es_trio(matriz)[0]:
			return [True,self.es_trio(matriz)[1],self.es_pareja(matriz)[1]]
		else:
			return [False]

	def es_escalera_color(self,matriz):
		_es_escalera_color = False
		contador_maximo = 0
		carta_mas_alta = -1
		palo_de_color = -1
		for palo in range(len(palos)):
			valor = 0
			contador = 0
			while valor < len(valores):
				if matriz[palo][valor] == 1:
					contador = contador + 1
					if contador_maximo < contador:
						contador_maximo = contador
						carta_mas_alta = valor
						palo_de_color = palo
				else:
					contador = 0
				valor = valor + 1
				if contador == 4 and valor ==len(valores):
					if matriz[palo][0]== 1:
						contador_maximo = 5
						carta_mas_alta = 13
						palo_de_color = palo
		
		if contador_maximo>= 5:
			return [True,carta_mas_alta,palo_de_color]

		else:
			return [False]

	def devuelve_carta_alta(self,matriz):
		maximo = 0
		indice_max = len(valores) - 1
		encontrado = False
		while indice_max > 0 and not encontrado:
			for j in range(len(palos)):
				if matriz[j][indice_max] == 1:
					maximo = indice_max
					encontrado = True
			indice_max = indice_max - 1

		i = 0
		hay_as = False
		while i < len(palos) and not hay_as:
			if matriz[i][0]== 1:
				maximo = 0
			i = i + 1

		return maximo



	

		




	def clasifica(self,mano,mesa):

		a_clasificar = self.transforma_a_mano(mano,mesa)
		matriz = self.crea_matriz_cartas(a_clasificar)

		if self.es_escalera_color(matriz)[0]:
			return [9,self.es_escalera_color(matriz)[1],self.es_escalera_color(matriz)[2]]
		elif self.es_poker(matriz)[0]:
			return [8,self.es_poker(matriz)[1]]
		elif self.es_full(matriz)[0]:
			return [7,self.es_full(matriz)[1],self.es_full(matriz)[2]]
		elif self.es_color(matriz)[0]:
			return [6,self.es_color(matriz)[1]]
		elif self.es_escalera(matriz)[0]:
			return [5,self.es_escalera(matriz)[1]]
		elif self.es_trio(matriz)[0]:
			return [4,self.es_trio(matriz)[1]]
		elif self.es_doble_pareja(matriz)[0]:
			return [3,self.es_doble_pareja(matriz)[1],self.es_doble_pareja(matriz)[2]]
		elif self.es_pareja(matriz)[0]:
			return [2,self.es_pareja(matriz)[1]]
		else:
			return [1,self.devuelve_carta_alta(matriz)]


	def compara(self, mano1, mano2, mesa):
		puntuacion1 = self.clasifica(mano1, mesa)
		puntuacion2 = self.clasifica(mano2, mesa)

		cadena1 = "El oponente 1 gana al 2."
		cadena2 = "El oponente 2 gana al 1."
		cadena3 = "El codigo no esta completo para que sepa cual gana."

		if puntuacion1[1] == 0:
			puntuacion1[1] = 13
		if puntuacion2[1] == 0:
			puntuacion2[1] = 13

		if puntuacion1[0] > puntuacion2[0]:

			print cadena1
			return 1

		elif puntuacion1[0] < puntuacion2[0]:

			print cadena2
			return -1

		else:
			if puntuacion1[1] > puntuacion2[1]:
				print cadena1
				return 1

			elif puntuacion1[1] < puntuacion2[1]:
				print cadena2
				return -1
			else:
				if len(puntuacion1) == 3:
					if puntuacion1[2] > puntuacion2[2]:
						print cadena1
						return 1
					elif puntuacion1[2] < puntuacion2[2]:
						print cadena2
						return -1
					else:
						print cadena3
						return 0
				else:
					print cadena3
					return 0

	def compara_testeo(self, mano1, mano2, mesa):
		puntuacion1 = self.clasifica(mano1, mesa)
		puntuacion2 = self.clasifica(mano2, mesa)

		if puntuacion1[1] == 0:
			puntuacion1[1] = 13
		if puntuacion2[1] == 0:
			puntuacion2[1] = 13

		if puntuacion1[0] > puntuacion2[0]:
			return 1

		elif puntuacion1[0] < puntuacion2[0]:
			return -1

		else:
			if puntuacion1[1] > puntuacion2[1]:
				return 1

			elif puntuacion1[1] < puntuacion2[1]:
				return -1
			else:
				if len(puntuacion1) == 3:
					if puntuacion1[2] > puntuacion2[2]:
	
						return 1
					elif puntuacion1[2] < puntuacion2[2]:
	
						return -1
					else:

						return 0
				else:
					return 0


