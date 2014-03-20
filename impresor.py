from baraja import *

from mano import *

from variables import *

class Impresor:
	def __init__(self):
		pass

	def imprime_mano(self,mano):
		a_imprimir = []
		cadena = ""
		for indice in range(mano.muestra_longitud()):
			una_carta = mano.muestra_carta(indice)
			cadena = una_carta.info()[0] + " de " + una_carta.info()[1]
			a_imprimir.append(cadena)

		print  "Esta es una mano:",a_imprimir

	def imprime_baraja(self,baraja):
		a_imprimir = []
		lista = baraja.muestra_baraja()
		for carta in lista:
			para_imprimir = carta.info()[0]+" de "+carta.info()[1]
			a_imprimir.append(para_imprimir)

		print a_imprimir

	def imprime_mesa(self,mesa):
		a_imprimir = []
		cadena = ""
		for indice in range(mesa.muestra_longitud()):
			una_carta = mesa.muestra_carta(indice)
			cadena = una_carta.info()[0] + " de " + una_carta.info()[1]
			a_imprimir.append(cadena)

		print "Esta es la mesa:",a_imprimir

	def imprime_puntuacion(self,puntuacion):
		if puntuacion[0] == 1:
			print "Tiene carta alta de",indice_a_valor(puntuacion[1])
		elif puntuacion[0] == 2:
			print "Tiene pareja de",indice_a_valor(puntuacion[1])
		elif puntuacion[0] == 3:
			print "Tiene dobles parejas de",indice_a_valor(puntuacion[1]),"y",indice_a_valor(puntuacion[2])
		elif puntuacion[0]== 4:
			print "Tiene trio de", indice_a_valor(puntuacion[1])
		elif puntuacion[0]== 5:
			print "Tiene escalera en",indice_a_valor(puntuacion[1])
		elif puntuacion[0] == 6:
			print "Tiene color (",indice_a_palo(puntuacion[1]),")"
		elif puntuacion[0]== 7:
			print "Tiene full de",indice_a_valor(puntuacion[1]),"y",indice_a_valor(puntuacion[2])
		elif puntuacion[0]==8:
			print "Tiene poker de",indice_a_valor(puntuacion[1])
		elif puntuacion[0]==9:
			print "Tiene escalera de color sobre",indice_a_valor(puntuacion[1]),"de",indice_a_palo(puntuacion[2])

