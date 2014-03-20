from baraja import *
from mano import *
from crupier import *
from variables import *
from impresor import *
from clasificador import * 


class Juego:
	def __init__(self):
		self.crupier = Crupier()
		self.impresor = Impresor()

	def imprime_actual(self,cadena):
		mesa = self.crupier.devuelve_mesa()
		op1 = self.crupier.devuelve_op1()
		op2 = self.crupier.devuelve_op2()

		print cadena

		self.impresor.imprime_mesa(mesa)
		self.impresor.imprime_mano(op1)
		self.impresor.imprime_mano(op2)
		print ""
	def testear_sin(self,carta):
		self.crupier.elimina_carta(carta)

	def utiliza_testeo(self,mano):
		self.crupier.reparte_testeo(mano)
		self.crupier.reparte_segunda_ronda()

		self.crupier.reparte_tercera_ronda()

		self.crupier.reparte_cuarta_ronda()

		self.crupier.clasifica_op1_testeo()
		self.crupier.clasifica_op2_testeo()

		ganador = self.crupier.compara_manos_testeo()

		self.crupier = Crupier()

		return ganador



	def juega(self):
		self.crupier.reparte_primera_ronda()

		self.crupier.reparte_segunda_ronda()

		self.crupier.reparte_tercera_ronda()

		self.crupier.reparte_cuarta_ronda()

		self.imprime_actual("Ultima ronda")

		self.crupier.clasifica_op1()
		self.crupier.clasifica_op2()

		ganador = self.crupier.compara_manos()
		
		print ""

		self.crupier = Crupier()

		return ganador
