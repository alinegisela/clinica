#Criacao da classe CONTROLE
from Cliente import Cliente
from Pacote import Pacote
from Venda import Venda
from Tratamento import Tratamento
from Funcionario import Funcionario
from login import Login
from datetime import date

class Controle:

    def __init__(self):

        self.listaClientes = []
        self.listaFuncionarios = []
        self.listaTratamentos = []
        self.listaVendas = []
        self.listaPacotes = []
        self.listaLogin = []
        self.carregar_dados()

    def carregar_dados(self):
        #as classes com composicao e listas, como ler?
        handleClientes = open("dados\\clientes.txt", "r")
        handleFuncionarios = open("dados\\funcionarios.txt", "r")
        handleTratamentos = open("dados\\tratamentos.txt", "r")
        handleVendas = open("dados\\vendas.txt", "r")
        handlePacotes = open("dados\\pacotes.txt", "r")
        handleLogin = open("dados\\login.txt", "r")
        
        for line in handleClientes:
            attr = line.split(', ')
            self.cadastrar_cliente(attr[0], attr[1], attr[2], attr[3], attr[4])

        for line in handleFuncionarios:
            atributos = line.split(', ')
            self.cadastrar_funcionario(attr[0], attr[1], attr[2], attr[3], attr[4], attr[5], attr[6], attr[7], attr[8])

        for line in handleTratamentos:
            attr = line.split(', ')
            self.cadastrar_tratamento(attr[0], attr[1])

        for line in handleVendas:
            attr = line.split(', ')
            self.cadastrar_venda(attr[0], attr[1], attr[2], attr[3])

        for line in handlePacotes:
            attr = line.split(', ')
            self.cadastrar_pacote(attr[0])

        for line in handleLogin:
            attr = line.split(', ')
            self.cadastrar_login(attr[0], attr[1])
            
        handleClientes.close()
        handleFuncionarios.close()
        handleTratamentos.close()
        handleVendas.close()
        handlePacotes.close()
        handleLogin.close()
        
    def salvar_dados(self):
        #as classes com composicao e listas, como armazenar?
        handleClientes = open("dados\\clientes.txt", "w")
        handleFuncionarios = open("dados\\funcionarios.txt", "w")
        handleTratamentos = open("dados\\tratamentos.txt", "w")
        handleVendas = open("dados\\vendas.txt", "w")
        handlePacotes = open("dados\\pacotes.txt", "w")
        handleLogin = open("dados\\login.txt", "w")

        cliente_string = ""
        for i in range(len(self.listaClientes)):
            c = self.listaClientes[i]
            cliente_string += c.nome + ", " + c.cpf + ", "+ c.endereco + ", "+ c.telefone + ", " + c.email
            cliente_string += "\n"
            
        func_string = ""
        for i in range(len(self.listaFuncionarios)):
            c = self.listaFuncionarios[i]
            func_string += c.nome + ", " + c.cpf + ", "+ c.endereco + ", "+ c.telefone + ", " + c.dt_nasc + ", " + c.email + ", " + c.cargo + ", " + c.salario
            func_string += "\n"
            
        tratamento_string = ""
        for i in range(len(self.listaTratamentos)):
            c = self.listaTratamentos[i]
            tratamento_string += c.nome + ", " + c.valor
            tratamento_string += "\n"
            
        venda_string = ""
        for i in range(len(self.listaVendas)):
            c = self.listaVendas[i]
            venda_string += c.cliente.cpf + ", " + c.pacote.id + ", "+ c.data + ", "+ c.valorTotal
            venda_string += "\n"
            
        pacote_string = ""
        for i in range(len(self.listaPacotes)):
            c = self.listaPacotes[i]
            
	    t = ""
            for k in range(self.listaPacotes.tratamentos):
	    	t += self.listaPacotes.tratamentos[k].id+"/ "
			
            pacote_string += c.total + ", " + t
            pacote_string += "\n"

        cliente_string = ""
        for i in range(len(self.listaLogin)):
            c = self.listaLogin[i]
            cliente_string += c.usuario + ", " + c.senha
            cliente_string += "\n"
            
        handleClientes.write(cliente_string)
        handleFuncionarios.write(func_string)
        handleTratamentos.write(tratamento_string)
        handleVendas.write(venda_string)
        handlePacotes.write(pacote_string)
        handleCliente.write(cliente_string)

        handleClientes.close()
        handleFuncionarios.close()
        handleTratamentos.close()
        handleVendas.close()
        handlePacotes.close()
        handleCliente.close()

    def cadastrar_tratamento(self, nome, valor):

        novo_tratamento = Tratamento(nome, valor)
        self.listaTratamentos.append(novo_tratamento)

    def cadastrar_pacote(self, id, total, lista_Tratamento):
        novo_pacote = Pacote(id, total, lista_Tratamento)
        self.listaPacotes.append(novo_pacote)

    def cadastrar_cliente(self, nome, cpf, endereco, telefone, email):

        novo_cliente = Cliente(nome, cpf, endereco, telefone, email)

        self.listaClientes.append(novo_cliente)

    def retornar_cliente(self, cpf):
        
        for i in range(len(self.listaClientes)):
            if self.listaClientes[i].cpf == cpf:
                cliente = self.listaClientes[i]
                return cliente
            
    def atualizar_cliente(self, nome, cpf, end, tel, email):
        cliente = self.retornar_cliente(cpf)
        cliente.nome = nome
        cliente.endereco = end
        cliente.telefone = tel
        cliente.email = email

    def deletar_cliente(self, cpf):
        cliente = self.retornar_cliente(cpf)
        self.listaClientes.remove(cliente)

    def cadastrar_venda(self, Cliente, Pacote, data, valorTotal):

        nova_venda = Venda(Cliente, Pacote, data, valorTotal)
        
        self.listaVendas.append(nova_venda)
        
    def listar_pacotes(self):
        #sorted: organiza lista em ordem crescente pelo atributo total
        pacotes_lucro = sorted(self.listaPacotes, key=lambda pacote: pacote.total)
        
        pacotes = ""
        for i in range(len(pacotes_lucro)-1, -1, -1):
            pacotes += pacotes_lucro[i].__str__() + "\n\n"
    
        return pacotes

    def listar_pacotes_cliente(self, cpf_cliente):
        pacotes = []

        for i in range(len(self.listaVendas)):
            if self.listaVendas[i].cpf_cliente == cpf_cliente:
                pacotes.append(self.listaVendas[i])

        return pacotes


    #retorna uma lista com os lucros por mes, a partir do mes da primeira venda
    def listar_lucro_mes(self):
        
        vendas = sorted(self.listaVendas, key=lambda venda: venda.data)
        mes_anterior = vendas[0].data.month
        ano_anterior = vendas[0].data.year
        lucro_mes =  vendas[0].valorTotal * 0.6
        lucros = []

        for i in range(1, len(vendas)):
            mes_atual = vendas[i].data.month
            ano_atual = vendas[i].data.year
                
            if ano_atual == ano_anterior and mes_atual == mes_anterior:
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
            
    def listar_lucro_ano(self):
        vendas = sorted(self.listaVendas, key=lambda venda: venda.data)
        ano_anterior = vendas[0].data.year
        lucro_ano = vendas[0].valorTotal * 0.6
        lucros = []
        
        for i in range(len(vendas)):
            ano_atual = vendas[i].data.year

            if ano_atual == ano_anterior:
                lucro_ano += vendas[i].valorTotal * 0.6
            else:
                lucros.append(lucro_ano)
                lucros_ano = 0

                diferenca_ano = ano_atual - ano_anterior

                for j in range(diferenca_ano-1):
                    lucros.append(0)

                ano_anterior = vendas[i].data.year
                lucro_ano = vendas[i].valorTotal * 0.6
        lucros.append(lucro_ano)
        return lucros

     #crud funcionarios
    def cadastrar_funcionario(self, nome, cpf, end, tel, dt_nasc, email, cargo, salario, senha):
        novo_funcionario = Funcionario(nome, cpf, end, tel, dt_nasc, email, cargo, salario)
        novo_login = Login(cpf, senha)
        self.listaFuncionarios.append(novo_funcionario)
        self.listaLogin.append(novo_login)
       
    def retornar_funcionario(self, cpf):
        
        for i in range(len(self.listaFuncionarios)):
            if self.listaFuncionarios[i].cpf == cpf:
                funcionario = self.listaFuncionarios[i]
                return funcionario
            
    def atualizar_funcionario(self, nome, cpf, end, tel, dt_nasc, email, cargo, salario):
        funcionario = self.retornar_funcionario(cpf)
        funcionario.nome = nome
        funcionario.endereco = end
        funcionario.telefone = tel
        funcionario.dt_nasc = dt_nasc
        funcionario.email = email
        funcionario.cargo = cargo
        funcionario.salario = salario
        
    def deletar_funcionario(self, cpf):
        funcionario = self.retornar_funcionario(cpf)
        self.listaFuncionarios.remove(funcionario)

    def cadastrar_login(self, usuario, senha):
        novo_login = Login(usuario, senha)
        self.listaLogin.append(novo_login)

    def login(self, usuario, senha):
        validar = False
        for i in range(len(self.listaFuncionarios)):
            if self.listaFuncionarios[i].cpf == usuario:
                for j in range(self.listaLogin):
                    if self.listaLogin[j].usuario == usuario:
                        if self.listaLogin[j].senha == senha:
                            validar = True
        

        return validar
