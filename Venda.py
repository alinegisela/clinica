#Classe Venda
from Cliente import Cliente
from Pacote import Pacote

class Venda:

    def __init__(self, cliente, pacote, data, valorTotal):
        self.cliente  = cliente
        self.pacote = pacote
        self.data = data
        self.valorTotal = valorTotal

   
