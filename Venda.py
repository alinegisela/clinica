#Classe Venda
from Cliente import Cliente
from Pacote import Pacote

class Venda:

    def __init__(self, cliente, pacote, data):
        # id random
	self.id = 0
        self.cliente  = Cliente
        self.pacote = Pacote
        self.data = data
        self.valorTotal = self.calc_total()

    def calc_total(self):
        valor = 0
        for i in range(len(self.pacote.tratamentos)):
            valor += self.pacote.tratamentos[i].valor
        return valor

   
