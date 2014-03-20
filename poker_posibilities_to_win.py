from juego import *
from baraja import *

juego = Juego()

palo1 = raw_input("Primera carta:palo ")
valor1 = raw_input("Primera carta:valor ")
palo2 = raw_input("Segunda carta:palo ")
valor2 = raw_input("Segunda carta:valor ")

n_testeos = int(raw_input("Numero de pruebas? :"))

carta1 = Carta(valor1,palo1)
carta2 = Carta(valor2, palo2)
mano = Mano([carta1,carta2])

ganados = 0

for i in range(n_testeos):
	juego.testear_sin(carta1)
	juego.testear_sin(carta2)

	marca = juego.utiliza_testeo(mano)

	if marca == 1:
		ganados = ganados +1

porcentaje = ganados*1.0/n_testeos

print "El porcentaje de ganar es :", porcentaje
