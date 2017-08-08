#Criacao da classe CONTROLE
from Cliente import Cliente
from Pacote import Pacote
from Venda import Venda
from Tratamento import Tratamento
from datetime import date

class Controle:

    def __init__(self):

        self.listaClientes = []
        self.listaFuncionarios = []
        self.listaTratamentos = []
        self.listaVendas = [ Venda(Cliente("aline", "123", "rua tal", "87", "aline@"), Pacote(200, Tratamento("tratamento 1 ", 200)), date(2017,3,15), 800), Venda(Cliente("aline", "123", "rua tal", "87", "aline@"), Pacote(200, Tratamento("tratamento 1 ", 200)), date(2017,1,15), 1000)]
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

    #retorna uma lista com os lucros por mes, a partir do mes da primeira venda
    def listar_lucro_mes(self):
        
        vendas = sorted(self.listaVendas, key=lambda venda: venda.data)
        mes_anterior = 0
        ano_anterior = 0
        lucro_mes = 0
        lucros = []

        for i in range(len(vendas)):
            mes_atual = vendas[i].data.month
            ano_atual = vendas[i].data.year
            if i == 0:
                
                mes_anterior = mes_atual
                ano_anterior = ano_atual
                lucro_mes += vendas[i].valorTotal * 0.6
                
            elif ano_atual == ano_anterior and mes_atual == mes_anterior:
                lucro_mes += vendas[i].valorTotal * 0.6
                
            else:
                
                lucros.append(lucro_mes)
                lucro_mes = 0

                diferenca_ano = ano_atual - ano_anterior
                diferenca_mes = mes_atual - mes_anterior

                for j in range((12 * diferenca_ano + diferenca_mes)-1):
                    lucros.append(0)
                
                ano_anterior = vendas[i].data.year
                mes_anterior = vendas[i].data.month
                lucro_mes = vendas[i].valorTotal * 0.6
                
        lucros.append(lucro_mes)
        return lucros        
            
        
