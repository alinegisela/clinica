#Criação da classe CONTROLE
from cliente import Cliente
from pacote import Pacote
from Tratamento import Tratamento
from venda import Venda

class Controle:

    def __init__(self):

        self.listaClientes = []
        self.listaFuncionarios = []
        self.listaTratamentos = []
        self.listaVendas = []
        self.listaPacotes = []

    def cadastrar_tratamento(self, nome, valor):

        novo_tratamento = Tratamento(nome, valor)
        self.listaTratamentos.append(novo_tratamento)

    def cadastrar_pacote(self, lista_Tramento):
        self.listaPacotes.append(lista_Tramento)

    def cadastrar_cliente(self, nome, cpf, endereco, telefone, email):

        novo_cliente = Cliente(nome, cpf, endereco, telefone, email)

        self.listaClientes.append(novo_cliente)

    def cadastrar_venda(self, cpf_cliente, Pacote, valorTotal):

        nova_venda = Venda(cpf_cliente, Pacote, data, valorTotal)
        
        self.listaVendas.append(nova_venda)
        
