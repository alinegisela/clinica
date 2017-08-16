#Criacao da classe CONTROLE
from Cliente import Cliente
from Pacote import Pacote
from Venda import Venda
from Tratamento import Tratamento
from Funcionario import Funcionario
from login import Login
from datetime import *
from random import randint

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
        print 'iniciando'
        
        #as classes com composicao e listas, como ler?
        handleClientes = open("dados\\clientes.txt", "r")
        handleFuncionarios = open("dados\\funcionarios.txt", "r")
        handleTratamentos = open("dados\\tratamentos.txt", "r")
        handleVendas = open("dados\\vendas.txt", "r")
        handlePacotes = open("dados\\pacotes.txt", "r")
        handleLogin = open("dados\\login.txt", "r")
      
        
        for line in handleClientes:
            attr = line.split(', ')
            attr2 = attr[4].split('\n')
            attr[4] = attr2[0]
            self.inserir_cliente(attr[0], attr[1], attr[2], attr[3], attr[4])

        for line in handleFuncionarios:
            
            attr = line.split(', ')
            attr2 = attr[7].split('\n')
            attr[7] = attr2[0]
            self.inserir_funcionario(attr[0], attr[1], attr[2], attr[3], attr[4], attr[5], attr[6], attr[7])

        for line in handleLogin:
            attr = line.split(', ')
            attr2 = attr[1].split('\n')
            attr[1] = attr2[0]
            self.cadastrar_login(attr[0], attr[1])

        for line in handleTratamentos:
            attr = line.split(', ')
            attr2 = attr[2].split('\n')
            attr[2] = attr2[0]
            self.inserir_tratamento(attr[0], attr[1], attr[2])

        

        #AQUI
        listaID = []
        for line in handlePacotes:
            attr = line.split(', ')
            
            #tirando o enter do ultimo atributo
            attr2 = attr[2].split('\n')
            attr[2] = attr2[0]
            #separando os tratamentos por id
            listaID = attr[2].split('/')
            self.inserir_pacote(attr[0], attr[1], listaID)

        for line in handleVendas:
            attr = line.split(', ')
            attr2 = attr[3].split('\n')
            attr[3] = attr2[0]
            self.inserir_venda(attr[0], attr[1], attr[2], attr[3])
            
        handleClientes.close()
        handleFuncionarios.close()
        handleTratamentos.close()
        handleVendas.close()
        handlePacotes.close()
        handleLogin.close()
        print len(self.listaVendas)

        self.salvar_dados()
    
        
    def salvar_dados(self):
        print 'salvando dados'
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
            tratamento_string += c.id+", "+c.nome + ", " + c.valor
            tratamento_string += "\n"

        
        venda_string = ""
        for i in range(len(self.listaVendas)):
            c = self.listaVendas[i]
            venda_string += str(c.id)+", " + str(c.cliente.cpf) + ", " + str(c.pacote.id) + ", "+ str(c.data) 
            venda_string += "\n"
        print venda_string

        #AQUI
        pacote_string = ""
        print len(self.listaPacotes)
        for i in range(len(self.listaPacotes)):
            
            c = self.listaPacotes[i]

            t = ""
            for k in range(len(c.tratamentos)):
                
                t += c.tratamentos[k].id
                if k != len(c.tratamentos)-1:
                    t+="/"
			
            pacote_string += str(c.id)+", "+str(c.total) + ", " + t
            pacote_string += "\n"

        login_string = ""
        for i in range(len(self.listaLogin)):
            c = self.listaLogin[i]
            login_string += c.usuario + ", " + c.senha
            login_string += "\n"
            
        handleClientes.write(cliente_string)
        handleFuncionarios.write(func_string)
        handleTratamentos.write(tratamento_string)
        handleVendas.write(venda_string)
        handlePacotes.write(pacote_string)
        handleLogin.write(login_string)

        handleClientes.close()
        handleFuncionarios.close()
        handleTratamentos.close()
        handleVendas.close()
        handlePacotes.close()
        handleLogin.close()

    def cadastrar_tratamento(self, id,nome, valor):

        novo_tratamento = Tratamento(id, nome, valor)
        self.listaTratamentos.append(novo_tratamento)
        self.salvar_dados()

    def inserir_tratamento(self, id,nome, valor):

        novo_tratamento = Tratamento(id, nome, valor)
        self.listaTratamentos.append(novo_tratamento)

    def buscar_tratamento(self, id):
        
        for i in range(len(self.listaTratamentos)):
            if self.listaTratamentos[i].id == id:
                tratamento = self.listaTratamentos[i]
                return tratamento

    def inserir_pacote(self, id, total, lista_ID):
       
        lista_Tratamento = []
        for i in range(len(lista_ID)):
            lista_Tratamento.append(self.buscar_tratamento(lista_ID[i]))
        
        novo_pacote = Pacote( id,total, lista_Tratamento)
        self.listaPacotes.append(novo_pacote)

        for i in range(len(self.listaPacotes)):
            print self.listaPacotes[i]

    def cadastrar_pacote(self,total, lista_pos):
       
        #id
        nova_id = False
        while nova_id == False:
            id = randint(1,100)
            if self.retornar_pacote(id) == False:
                nova_id = True
        
        lista_Tratamento = []
        #pela pos
        for i in range(len(lista_pos)):
            lista_Tratamento.append(self.listaTratamentos[ int(lista_pos[i]) ])
        
        novo_pacote = Pacote( id,total, lista_Tratamento)
        self.listaPacotes.append(novo_pacote)
        self.salvar_dados()

        print self.listaPacotes[len(self.listaPacotes)-1]

    def retornar_pacote(self, id):
        
        for i in range(len(self.listaPacotes)):
            print 'IDS DA LISTAAA ' +str(self.listaPacotes[i].id)
            if self.listaPacotes[i].id == id:
                pacote = self.listaPacotes[i]
                return pacote
        return False
        
   
    def cadastrar_cliente(self, nome, cpf, endereco, telefone, email):

        novo_cliente = Cliente(nome, cpf, endereco, telefone, email)

        self.listaClientes.append(novo_cliente)
        self.salvar_dados()
        
    def inserir_cliente(self, nome, cpf, endereco, telefone, email):

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

        self.salvar_dados()

    def deletar_cliente(self, cpf):
        cliente = self.retornar_cliente(cpf)
        self.listaClientes.remove(cliente)

    def deletar_pacote(self, lista_selec):
        pac = self.listar_pacotes_lucro()
        ids = []


        for i in range(len(lista_selec)):
            indice = len(pac)-1-int(lista_selec[i])
            
            id_pac = pac[indice].id
            
            ids.append(id_pac)

        for i in range(len(ids)):
            self.listaPacotes.remove(self.retornar_pacote(ids[i]))

        self.salvar_dados()
            
    def cadastrar_venda(self, cpf_cliente, indice):
        #id
        nova_id = False
        while nova_id == False:
            idd = randint(1,100)
            if self.retornar_pacote(idd) == False:
                nova_id = True
        
        pac = self.listar_pacotes_lucro()
        ind = len(pac)-1-int(indice)
        id_pac = pac[ind].id

        data = date.today().strftime("%d/%m/%y")
        nova_venda = Venda(idd, self.retornar_cliente(cpf_cliente), self.retornar_pacote(id_pac), data)
        
        self.listaVendas.append(nova_venda)
        print'vendaaaaaaaaaaaaaa'+ str(nova_venda.id)
        print'vendaaaaaaaaaaaaaa'+self.listaVendas[0].cliente.__str__()
        self.salvar_dados()


    def inserir_venda(self, id, cpf_cliente, id_pacote, data):
        print 'ID PACOTE ' + str(id_pacote)
        if self.retornar_pacote(id_pacote) != False:
            nova_venda = Venda(id, self.retornar_cliente(cpf_cliente), self.retornar_pacote(id_pacote), data)
        
            self.listaVendas.append(nova_venda)
        
    def listar_pacotes(self):
        #sorted: organiza lista em ordem crescente pelo atributo total
        pacotes_lucro = sorted(self.listaPacotes, key=lambda pacote: pacote.total)
       
        pacotes = ""
        for i in range(len(pacotes_lucro)-1, -1, -1):
            pacotes += "Pacote "+str(len(pacotes_lucro)-i)+"\n" 
            pacotes += pacotes_lucro[i].__str__() + "\n\n"
            print 'Listando os pacotes:\t' + pacotes_lucro[i].__str__()+"\n\n"
        return pacotes

    def listar_pacotes_lucro(self):
        #sorted: organiza lista em ordem crescente pelo atributo total
        pacotes_lucro = sorted(self.listaPacotes, key=lambda pacote: pacote.total)
        print "socorro deus "+ pacotes_lucro[0].__str__()
        return pacotes_lucro
    
    def listar_tratamentos(self):
        #sorted: organiza lista em ordem crescente pelo atributo total
        pacotes_lucro = sorted(self.listaTratamentos, key=lambda tratamento: tratamento.valor)
        
        pacotes = ""
        for i in range(len(pacotes_lucro)-1, -1, -1):
            pacotes += pacotes_lucro[i].__str__() + "\n\n"
        print pacotes
        return pacotes

    def retornar_tratamentos(self):
        trat = self.listaTratamentos
        return trat
        

    def listar_pacotes_cliente(self, cpf_cliente):
        pacotes = []

        for i in range(len(self.listaVendas)):
            if self.listaVendas[i].cliente.cpf == cpf_cliente:
                pacotes.append(self.listaVendas[i])

        return pacotes

    def listar_venda_cliente(self, cpf_cliente):
        vendas = self.listar_pacotes_cliente(cpf_cliente)
        vendas_str = ""
        for i in range(len(vendas)):
            vendas_str += vendas[i].__str__()
        return vendas_str

    def listar_mes(self):
        lucro_str = ""
        vendas = self.listaVendas
        for i in range(len(vendas)):
            vendas[i].data = datetime.strptime(vendas[i].data, '%d/%m/%y')
        vendas = sorted(self.listaVendas, key=lambda venda: venda.data)
        dt_inicial = vendas[0].data
        dt_final = vendas[len(vendas)-1].data
        qtd_ano = (dt_final.year - dt_inicial.year)+1
        lucro = [[0 for x in range(12)] for y in range(qtd_ano) ]
        

        for i in range(len(vendas)):
            data_f = vendas[i].data
            mes = data_f.month
            ano = data_f.year - dt_inicial.year
            lucro[ano][mes-1] += vendas[i].pacote.lucro

        for i in range(qtd_ano):
            for j in range(12):
                if lucro[i][j] != 0:
                    mes =""
                    if j<10:
                        mes = "0"+str(j+1)
                    else:
                        mes = str(j+1)
                    lucro_str+= mes+"/"+str(i+dt_inicial.year)+" - R$ "+str(lucro[i][j])+"\n"
        print lucro_str
        for i in range(len(vendas)):
            vendas[i].data = datetime.strftime(vendas[i].data, '%d/%m/%y')
        return lucro_str
    
    def listar_ano(self):
        lucro_str = ""
        vendas = self.listaVendas
        
        if type(vendas[0].data) != type(date.today()):
            for i in range(len(vendas)):
                vendas[i].data = datetime.strptime(vendas[i].data, '%d/%m/%y')
        vendas = sorted(self.listaVendas, key=lambda venda: venda.data)
        dt_inicial = vendas[0].data
        dt_final = vendas[len(vendas)-1].data
        qtd_ano = (dt_final.year - dt_inicial.year)+1
        lucro = [0 for y in range(qtd_ano) ]
        
        for i in range(len(vendas)):
            data_f = vendas[i].data
            
            ano = data_f.year - dt_inicial.year
            lucro[ano] += vendas[i].pacote.lucro

        for i in range(qtd_ano):
            if lucro[i]!= 0:
                lucro_str+= str(i+dt_inicial.year)+" - R$ "+str(lucro[i])+"\n"
        print lucro_str
        for i in range(len(vendas)):
            vendas[i].data = datetime.strftime(vendas[i].data, '%d/%m/%y')
        return lucro_str
        return lucro_str
            

     #crud funcionarios
    def cadastrar_funcionario(self, nome, cpf, end, tel, dt_nasc, email, cargo, salario, senha):
        novo_funcionario = Funcionario(nome, cpf, end, tel, dt_nasc, email, cargo, salario)
        novo_login = Login(cpf, senha)
        self.listaFuncionarios.append(novo_funcionario)
        self.listaLogin.append(novo_login)

    def inserir_funcionario(self, nome, cpf, end, tel, dt_nasc, email, cargo, salario):
        novo_funcionario = Funcionario(nome, cpf, end, tel, dt_nasc, email, cargo, salario)
        
        self.listaFuncionarios.append(novo_funcionario)
      
        
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
        funcionario.senha = senha

        
    def deletar_funcionario(self, cpf):
        funcionario = self.retornar_funcionario(cpf)
        self.listaFuncionarios.remove(funcionario)

    def cadastrar_login(self, usuario, senha):
        
        novo_login = Login(usuario, senha)
        self.listaLogin.append(novo_login)

    def login(self, usuario, senha):
        validar = [False, False]
       
        for i in range(len(self.listaFuncionarios)):
            
            if self.listaFuncionarios[i].cpf == usuario:
                
                for j in range(len(self.listaLogin)):
                    
                    if self.listaLogin[j].usuario == usuario:
                        
                        if self.listaLogin[j].senha == senha:
                            validar[0] = True
                           
                            break
                        
                if validar[0]==True:
                    if self.listaFuncionarios[i].cargo == 'gerente':
                        validar[1] = True
                    return validar
        
        print validar
        return validar

    
