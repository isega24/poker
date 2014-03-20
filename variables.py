palos = ["picas", "rombos", "corazones", "treboles"]
valores = ["As", "2", "3", "4", "5", "6" , "7", "8", "9", "10", "J", "Q", "K"]
MAX_MANO = 5
N_CARTAS = len(palos)*len(valores)

def maximo_lista(lista):
	indice = 0
	maximo = lista[indice]

	for i in range(len(lista)):
		if maximo < lista[i]:
			maximo = lista[i]
			indice = i

	return indice

def segundo_maximo_lista(lista):
	del lista[maximo_lista(lista)]

	return maximo_lista(lista)

def indice_a_valor(indice):
	if indice == 0:
		return "As"
	elif indice == 12:
		return "K"
	elif indice == 11:
		return "Q"
	elif indice == 10:
		return "J"
	elif indice  <= 9:
		return "" + str(indice + 1)

def indice_a_palo(indice):
	return palos[indice]
