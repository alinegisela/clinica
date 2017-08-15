#Classe Venda
from Cliente import Cliente
from Pacote import Pacote

class Venda:

    def __init__(self, id, cliente, pacote, data):
        # id random
	self.id = id
        self.cliente  = cliente
        self.pacote = pacote
        self.data = data
        self.valorTotal = self.calc_total()

    def calc_total(self):
        valor = 0.0
        for i in range(len(self.pacote.tratamentos)):
            valor += float(self.pacote.tratamentos[i].valor)
        return valor

    def __str__(self):
        return "Venda - " +str(self.id)+"\nCliente: "+self.cliente.nome+"\nCpf: "+self.cliente.cpf+"\nData da venda: "+self.data+"\n"+self.pacote.__str__()
       
