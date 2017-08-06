#Criacao da classe CONTROLE
from Cliente import Cliente
from Pacote import Pacote
from Tratamento import Tratamento

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
        
    def listar_pacotes(self):
        #sorted: organiza lista em ordem crescente pelo atributo total
        pacotes_lucro = sorted(self.listaPacotes, key=lambda pacote: pacote.total)
        
        pacotes = ""
        for i in range(len(pacotes_lucro)-1, -1, -1):
            pacotes += pacotes_lucro[i].__str__() + "\n\n"
    
        return pacotes

