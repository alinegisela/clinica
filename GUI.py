import Tkinter as tk
from controle import Controle

class SampleApp(tk.Frame):

    def __init__(self,janela ,*args, **kwargs):
        tk.Frame.__init__(self,janela, *args, **kwargs)
        self.root  = janela
        self.controle = Controle()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(janela)
        self.frame= tk.Frame(janela, height=600, width=380)
        self.frame.place(x=100)
        #container.pack(side='top', expand=True)
        container.place(x=100, y=50)
        container.lift()
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)
        self.pack_propagate(0)

        janela.title("Clinica Sinta-se Bem")
        janela.geometry("600x600")
        janela.configure(background='Beige')
        janela.resizable(0,0)
        #janela.configure(backgr.grid_bg='Beige'
        #self.menu = Menu_(self.root, self)
        #self.frame= tk.Frame(janela, height=600, width=320)
        #self.frame.pack()

        self.frames = {}
        for F in (Cadastrar_cliente,Atualizar_cliente, Retornar_cliente, Deletar_cliente, Login, Inicio, Cadastrar_venda, Recuperar_pacotes, Inicio_gerente, Cadastrar_pacote, Deletar_pacote, Listar_venda, Lucro, Cadastrar_Funcionario,Atualizar_Funcionario,Recuperar_Funcionario, Deletar_Funcionario):
            page_name = F.__name__
            frame = F(parent=container, controller=self, root=self.root, controle=self.controle)
            frame.height = 900
            self.frames[page_name] = frame
           

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            
            frame.grid(row=0, column=0, sticky="nsew")
            #frame.grid_rowconfigure(0, weight=1)
            #frame.grid_columnconfigure(0, weight=1)
            
            #self.grid_propagate(0)

      
        self.show_frame("Login")
        
  

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.height=600
        frame.update()
        frame.tkraise()
    def menu_gerente(self, page_name):
        frame = self.frames[page_name]
        frame.updateGerente()
        frame.tkraise()


class Cadastrar_cliente(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()

        

        self.nome = tk.Label(self, text='Nome')
        self.nome_str = tk.StringVar()
        self.nome_input = tk.Entry(self, textvariable = self.nome_str)

        self.cpf = tk.Label(self, text='Cpf')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)


        self.endereco = tk.Label(self, text='Endereco')
        self.endereco_str = tk.StringVar()
        self.endereco_input = tk.Entry(self, textvariable = self.endereco_str)
    
        self.telefone = tk.Label(self, text='Telefone')
        self.telefone_str = tk.StringVar()
        self.telefone_input = tk.Entry(self, textvariable = self.telefone_str)

        self.email = tk.Label(self, text='Email')
        self.email_str = tk.StringVar()
        self.email_input = tk.Entry(self, textvariable = self.email_str)

        self.nome.grid(row=1)
        self.nome_input.grid(row=1, column=1)
        self.cpf.grid(row=2)
        self.cpf_input.grid(row=2, column=1)
        self.endereco.grid(row=3)
        self.endereco_input.grid(row=3, column=1)
        self.telefone.grid(row=4)
        self.telefone_input.grid(row=4, column=1)
        self.email.grid(row=5)
        self.email_input.grid(row=5, column=1)
        
        
        self.b = tk.Button(self, text='Cadastrar cliente', command=self.acao)
        self.b.grid(row=6, column=1)
        
        
        
    def acao(self):
        self.controle.cadastrar_cliente(self.nome_str.get(), self.cpf_str.get(), self.endereco_str.get(), self.telefone_str.get(), self.email_str.get() )
        self.controller.show_frame("Inicio")


class Login(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
       
        #self.controle = Controle()

        root.config(menu=tk.Menu(root))
        
        self.txt = tk.Label(self, text='Digite seu CPF e sua senha: ')

        self.usuario = tk.Label(self, text='Usuario: ')
        self.usuario_str = tk.StringVar()
        self.usuario_input = tk.Entry(self, textvariable = self.usuario_str)

        self.senha = tk.Label(self, text='Senha: ')
        self.senha_str = tk.StringVar()
        self.senha_input = tk.Entry(self, textvariable = self.senha_str)

        self.txt.grid(row=1)
        self.usuario.grid(row=2)
        self.usuario_input.grid(row=2, column=1)
        self.senha.grid(row=3)
        self.senha_input.grid(row=3, column=1)
        
        self.b = tk.Button(self, text='Enviar', command=self.acao)
        self.b.grid(row=6, column=1)
        
        
    #add o else
    def acao(self):
        
        validar = self.controle.login(self.usuario_str.get(), self.senha_str.get())
        if validar[0] == True and validar[1] == True:
            self.controller.show_frame("Inicio_gerente")
        elif validar[0] == True and validar[1] == False:
            
            self.controller.show_frame("Inicio")

        

class Atualizar_cliente(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()

        self.nome = tk.Label(self, text='Nome')
        self.nome_str = tk.StringVar()
        self.nome_input = tk.Entry(self, textvariable = self.nome_str)

        self.cpf = tk.Label(self, text='Cpf')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)

        self.endereco = tk.Label(self, text='Endereco')
        self.endereco_str = tk.StringVar()
        self.endereco_input = tk.Entry(self, textvariable = self.endereco_str)
    
        self.telefone = tk.Label(self, text='Telefone')
        self.telefone_str = tk.StringVar()
        self.telefone_input = tk.Entry(self, textvariable = self.telefone_str)

        self.email = tk.Label(self, text='Email')
        self.email_str = tk.StringVar()
        self.email_input = tk.Entry(self, textvariable = self.email_str)

        self.nome.grid(row=1)
        self.nome_input.grid(row=1, column=1)
        self.cpf.grid(row=2)
        self.cpf_input.grid(row=2, column=1)
        self.endereco.grid(row=3)
        self.endereco_input.grid(row=3, column=1)
        self.telefone.grid(row=4)
        self.telefone_input.grid(row=4, column=1)
        self.email.grid(row=5)
        self.email_input.grid(row=5, column=1)
        
        
        self.b = tk.Button(self, text='Atualizar dados do cliente', command=self.acao)
        self.b.grid(row=6, column=1)
        
        
        
    def acao(self):
        print self.controle.listaClientes[0]
        self.controle.atualizar_cliente(self.nome_str.get(), self.cpf_str.get(), self.endereco_str.get(), self.telefone_str.get(), self.email_str.get() )
        print self.controle.listaClientes[0]
        self.controller.show_frame("Inicio")

global cpf
cpf = 'a'
class Retornar_cliente(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()
        

        self.cpfText = tk.Label(self, text='Cpf: ')
        self.cpf_str = tk.StringVar()
        self.cpf_inpt = tk.Entry(self, textvariable = self.cpf_str)
        
        
        self.b = tk.Button(self, text='OK', command=self.buscar)     
        self.nome = tk.StringVar()
        self.nome_input = tk.Label(self, textvariable=self.nome)
        
        self.cpf = tk.StringVar()
        self.cpf_input = tk.Label(self, textvariable = self.cpf)

        self.endereco = tk.StringVar()
        self.endereco_input = tk.Label(self, textvariable = self.endereco)
        
        self.telefone = tk.StringVar()
        self.telefone_input = tk.Label(self, textvariable = self.telefone)
        
        self.email = tk.StringVar()
        self.email_input = tk.Label(self, textvariable = self.email)
        

        self.cpfText.grid(row=1)
        self.cpf_inpt.grid(row=1, column=1)
        self.b.grid(row=2, column=1)
        self.nome_input.grid(row=3, column=1)
        self.cpf_input.grid(row=4, column=1)
        self.endereco_input.grid(row=5, column=1)
        self.telefone_input.grid(row=6, column=1)
        self.email_input.grid(row=7, column=1)
        
        
        
    def buscar(self):
        self.cliente = self.controle.retornar_cliente(self.cpf_str.get())
       
        self.nome.set("Nome: " + self.cliente.nome)
        self.cpf.set("Cpf: " + self.cliente.cpf)
        self.endereco.set("Endereco: " + self.cliente.endereco)
        self.telefone.set("Telefone: " + self.cliente.telefone)
        self.email.set("Email: " + self.cliente.email)

class Deletar_cliente(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()

        #self.menu = Menu_(self.root, self)

        self.texto = tk.Label(self, text='Digite o Cpf do cliente')

        self.cpf = tk.Label(self, text='Cpf')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)

        self.texto.grid(row=1)
        self.cpf.grid(row=2, column=0)
        self.cpf_input.grid(row=2, column=1)
              
        self.b = tk.Button(self, text='Deletar todos os dados do cliente', command=self.acao)
        self.b.grid(row=3, column=1)
        
        
        
    def acao(self):
       
        self.controle.deletar_cliente(self.cpf_str.get() )


  
class Inicio(tk.Frame):
    
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()
        
        self.cliente = self.controle.retornar_cliente( cpf)

        self.nome = tk.Label(self, text="Bem vindo(a) "+self.cliente.nome+"! O que voce deseja fazer?")
        
        self.nome.grid(row=1)
        
      
        self.b1 = tk.Button(self, text="Registrar uma venda",
                            command=lambda: controller.show_frame("Cadastrar_venda"))
        self.b2 = tk.Button(self, text="Cadastrar novo cliente",
                            command=lambda: controller.show_frame("Cadastrar_cliente"))
        self.b3 = tk.Button(self, text="Ver pacotes de tratamentos disponiveis",
                            command=lambda: controller.show_frame("Recuperar_pacotes"))
        self.b1.grid()
        self.b2.grid()
        self.b3.grid()
    def update(self):
      
        self.menu = Menu_(self.root, self.controller)
    def updateGerente(self):
        
        self.menu = Menu_(self.root, self.controller).menu
        subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Cadastrar novo cliente', command=lambda : controller.show_frame("Cadastrar_cliente"))
        subMenu.add_command(label='Atualizar dados de um cliente', command=lambda : controller.show_frame("Atualizar_cliente"))
        subMenu.add_command(label='Buscar um cliente', command=lambda : controller.show_frame("Retornar_cliente"))
    
class Inicio_gerente(tk.Frame):
    
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()
        
        self.cliente = self.controle.retornar_cliente( cpf)

        self.nome = tk.Label(self, text="Bem vindo(a) "+self.cliente.nome+"! O que voce deseja fazer?")
        
        self.nome.grid(row=1)
        
      
        self.b1 = tk.Button(self, text="Registrar uma venda",
                            command=lambda: controller.show_frame("Cadastrar_venda"))
        self.b2 = tk.Button(self, text="Cadastrar novo cliente",
                            command=lambda: controller.show_frame("Cadastrar_cliente"))
        self.b3 = tk.Button(self, text="Ver pacotes de tratamentos disponiveis",
                            command=lambda: controller.show_frame("Recuperar_pacotes"))
        self.b1.grid()
        self.b2.grid()
        self.b3.grid()
    def update(self):
      
        self.menu = Menu_gerente(self.root, self.controller).menu
        
    

#Cadastro de Venda
class Cadastrar_venda(tk.Frame):
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        self.cpf = tk.Label(self, text='Cpf do cliente: ')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)

        #mudar para listbox
        self.pacote = tk.Label(self, text='Codigo do pacote')
        self.pacote_str = tk.StringVar()
        self.pacote_input = tk.Entry(self, textvariable = self.pacote_str)

        self.lb_opcao = tk.StringVar()
        self.lb = tk.Listbox(self, listvariable=self.lb_opcao, height=4, selectmode=tk.SINGLE)

        self.tamanho = len(self.controle.listaPacotes)
        
        for i in range(self.tamanho):
            self.lb.insert(i+1, "Pacote "+str(i+1))
      
        self.lb.grid()
        self.pacotes = tk.StringVar()
        self.nome = tk.Label(self, textvariable=self.pacotes)
        self.nome.grid(row=2)
        
        self.cpf.grid(row=1)
        self.cpf_input.grid(row=1, column=1)
        self.pacote.grid(row=2)
        self.pacote_input.grid(row=2, column=1)
 
        
        self.b = tk.Button(self, text='Registrar venda', command=self.acao)
        self.b.grid(row=3, column=1)
        
        
        
    def acao(self):
        indice = self.lb.curselection()
        self.controle.cadastrar_venda(self.cpf_str.get(), indice[0])
        self.controller.show_frame("Inicio")

    def inserir_lb(self, tamanho):
        for i in range(tamanho):
            self.lb.insert(i+1, "Pacote "+str(i+1))

    def update(self):
        print 'update'
        self.pacotes.set(self.controle.listar_pacotes())
        print self.tamanho
        print 'tamanho da lista - ' + str(len(self.controle.listaPacotes))
        if self.tamanho != len(self.controle.listaPacotes):
           self.lb.delete(0, self.lb.size())
           tamanho = len(self.controle.listaPacotes)
           self.inserir_lb(tamanho)
        self.tamanho = len(self.controle.listaPacotes)

class Listar_venda(tk.Frame):
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        self.texto = tk.Label(self, text='Digite o CPF do cliente')

        self.cpf = tk.Label(self, text='CPF: ')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)

        self.texto.grid(row=1)
        self.cpf.grid(row=2, column=0)
        self.cpf_input.grid(row=2, column=1)
              

        self.vendas = tk.StringVar()
        
        self.titulo = tk.Label(self, text="Lista de pacotes adquiridos")
        self.nome = tk.Label(self, textvariable=self.vendas)
        
        self.titulo.grid(row=4)
        self.nome.grid(row=5)

        self.b = tk.Button(self, text='OK', command=self.acao)
        self.b.grid(row=3, column=1)
        
    def acao(self):
        self.vendas.set(self.controle.listar_venda_cliente(self.cpf_str.get()))
      

    def update(self):
        print 'update'
        self.vendas.set("")

class Lucro(tk.Frame):
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        
        self.var = tk.IntVar()
        
        self.R1 = tk.Radiobutton(self, text="Lucro anual", variable=self.var, value=1,
                  command=self.update)

        self.R2 = tk.Radiobutton(self, text="Lucro mensal", variable=self.var, value=2,
                  command=self.update)


        self.lucro = tk.StringVar()
        
       # self.titulo = tk.Label(self, text="Lucro por ano")
        self.nome = tk.Label(self, textvariable=self.lucro)

        self.R1.grid()
        self.R2.grid()
        #self.titulo.grid(row=1)
        self.nome.grid(row=2)
        
        
        #alterar os commands

    def update(self):
        print 'update'
        if self.var.get() == 1:
            self.lucro.set(self.controle.listar_ano())
        elif self.var.get() == 2:
            self.lucro.set(self.controle.listar_mes())
        print self.controle.listar_pacotes()
        
        
class Cadastrar_pacote(tk.Frame):
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()


        #mudar para listbox
        self.lb_opcao = tk.StringVar()
        self.lb = tk.Listbox(self, listvariable=self.lb_opcao, height=4, selectmode=tk.MULTIPLE)

        self.trat = self.controle.retornar_tratamentos()

        for i in range(len(self.trat)):
            print 'jesus'
            self.lb.insert(i+1, self.trat[i].nome)
            
        
        self.lb.grid()

        
        self.b = tk.Button(self, text='Cadastrar pacote', command=self.acao)
        self.b.grid(row=3, column=1)
        
        
        
    def acao(self):
        lista = self.lb.curselection()
        
        trat_selec = []
        total = 0;
        for i in range(len(lista)):
            trat_selec.append(lista[i])
            total += int(self.trat[int(lista[i])].valor)
        print 'aaaa'
        self.controle.cadastrar_pacote(total, trat_selec)
        print 'bbb'
        self.controller.show_frame("Inicio")



    
class Recuperar_pacotes(tk.Frame):
    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()

        self.pacotes = tk.StringVar()
        
        self.titulo = tk.Label(self, text="Lista de pacotes por lucro")
        self.nome = tk.Label(self, textvariable=self.pacotes)
        
        self.titulo.grid(row=1)
        self.nome.grid(row=2)
        
        
        #alterar os commands

    def update(self):
        print 'update'
        self.pacotes.set(self.controle.listar_pacotes())
        print self.controle.listar_pacotes()
        
        
      

class Deletar_pacote(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()

        #self.menu = Menu_(self.root, self)
        
        self.lb_opcao = tk.StringVar()
        self.lb = tk.Listbox(self, listvariable=self.lb_opcao, height=4, selectmode=tk.MULTIPLE)

        self.tamanho = len(self.controle.listaPacotes)
        for i in range(self.tamanho):
            self.lb.insert(i+1, "Pacote "+str(i+1))

      
        self.lb.grid()

        self.b = tk.Button(self, text='Deletar pacote(s)', command=self.acao)
        self.b.grid(row=3, column=1)
        
        self.pacotes = tk.StringVar()
        
       
        self.nome = tk.Label(self, textvariable=self.pacotes)
        
        self.nome.grid(row=2)

    

    def inserir_lb(self, tamanho):
        for i in range(tamanho):
            self.lb.insert(i+1, "Pacote "+str(i+1))

    def update(self):
        print 'update'
        self.pacotes.set(self.controle.listar_pacotes())
        print self.tamanho
        print 'tamanho da lista - ' + str(len(self.controle.listaPacotes))
        if self.lb.size() != len(self.controle.listaPacotes):
           self.lb.delete(0, self.lb.size())
           tamanho = len(self.controle.listaPacotes)
           self.inserir_lb(tamanho)
        
        
    def acao(self):

        lista = self.lb.curselection()
        trat_selec = []
        
        for i in range(len(lista)):
            trat_selec.append(lista[i])
            
        self.controle.deletar_pacote(trat_selec)
        self.controller.show_frame("Inicio")
        

  
    
class Menu_(tk.Frame):
  
    def theend():
        global janela
        janela.destroy()
    

    #MENU
    
    def __init__(self, master, controller):
       
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.controle = Controle()

      
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        master.title('')

        subMenu = tk.Menu(self.menu)

        self.menu.add_command(label='Inicio',command=lambda : controller.show_frame("Inicio"))
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Cadastrar novo cliente', command=lambda : controller.show_frame("Cadastrar_cliente"))
        subMenu.add_command(label='Atualizar dados de um cliente', command=lambda : controller.show_frame("Atualizar_cliente"))
        subMenu.add_command(label='Buscar um cliente', command=lambda : controller.show_frame("Retornar_cliente"))
        subMenu.add_command(label='Listar vendas de um cliente', command=lambda : controller.show_frame("Listar_venda"))

        subMenu2 = tk.Menu(self.menu)

        self.menu.add_cascade(label='Pacotes', menu=subMenu2)
        subMenu2.add_command(label='Cadastrar novo pacote', command=lambda : controller.show_frame("Cadastrar_pacote"))
        subMenu2.add_command(label='Excluir pacote', command=lambda : controller.show_frame("Deletar_pacote"))

        subMenu3 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Vendas', menu=subMenu3)
        subMenu3.add_command(label='Registrar nova venda', command=lambda : controller.show_frame("Cadastrar_venda"))
        subMenu3.add_command(label='Lucro anual/mensal', command=lambda : controller.show_frame("Lucro"))
     
        
        
        subMenu.add_separator()
        
        subMenu.add_command(label='Sair',command=self.theend)

class Menu_gerente(tk.Frame):
  
    def theend():
        global janela
        janela.destroy()
    

    #MENU
    
    def __init__(self, master, controller):
       
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.controle = Controle()

      
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        master.title('')

        subMenu = tk.Menu(self.menu)

        self.menu.add_command(label='Inicio',command=lambda : controller.show_frame("Inicio_gerente"))
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Cadastrar novo cliente', command=lambda : controller.show_frame("Cadastrar_cliente"))
        subMenu.add_command(label='Atualizar dados de um cliente', command=lambda : controller.show_frame("Atualizar_cliente"))
        subMenu.add_command(label='Buscar um cliente', command=lambda : controller.show_frame("Retornar_cliente"))
        subMenu.add_command(label='Listar vendas de um cliente', command=lambda : controller.show_frame("Listar_venda"))

        subMenu2 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Pacotes', menu=subMenu2)
        subMenu2.add_command(label='Cadastrar novo pacote', command=lambda : controller.show_frame("Cadastrar_pacote"))
        subMenu2.add_command(label='Excluir pacote', command=lambda : controller.show_frame("Deletar_pacote"))

        subMenu3 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Vendas', menu=subMenu3)
        subMenu3.add_command(label='Registrar nova venda', command=lambda : controller.show_frame("Cadastrar_venda"))
        subMenu3.add_command(label='Lucro anual/mensal', command=lambda : controller.show_frame("Lucro"))
        
        subMenu4 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Funcionarios', menu=subMenu4)
        subMenu4.add_command(label='Cadastrar novo funcionario', command=lambda : controller.show_frame("Cadastrar_Funcionario"))
        subMenu4.add_command(label='Atualizar dados de um funcionario', command=lambda : controller.show_frame("Atualizar_Funcionario"))
        subMenu4.add_command(label='Buscar funcionario', command=lambda : controller.show_frame("Recuperar_Funcionario"))
        subMenu4.add_command(label='Excluir funcionario', command=lambda : controller.show_frame("Deletar_Funcionario"))
        
        subMenu.add_separator()
        subMenu.add_command(label='Sair',command=self.theend)

class Cadastrar_Funcionario(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        
        self.labelname= tk.Label(self, text='Nome')
        #self.labelname.place(x=0,y=30)
        self.labelname.grid(row=1)
        self.name_str= tk.StringVar()
        self.entryname= tk.Entry(self, textvariable= self.name_str, width=40)
        self.entryname.grid(row=1, column=1)

        self.labelcpf= tk.Label(self, text='Cpf')
        self.labelcpf.grid(row=3)
        self.cpf_str= tk.StringVar()
        self.entrycpf= tk.Entry(self, textvariable= self.cpf_str, width=40)
        self.entrycpf.grid(row=3, column=1)

        self.labelendereco= tk.Label(self, text='Endereco')
        self.labelendereco.grid(row=4)
        self.endereco_str= tk.StringVar()
        self.entryendereco= tk.Entry(self, textvariable= self.endereco_str, width=40)
        self.entryendereco.grid(row=4, column=1)

        self.labeltelefone= tk.Label(self, text='Telefone')
        self.labeltelefone.grid(row=5)
        self.telefone_str= tk.StringVar()
        self.entrytelefone= tk.Entry(self, textvariable= self.telefone_str, width=40)
        self.entrytelefone.grid(row=5, column=1)

        self.labeldt_nasc= tk.Label(self, text='dt_nasc')
        self.labeldt_nasc.grid(row=6)
        self.dt_nasc_str= tk.StringVar()
        self.entrydt_nasc= tk.Entry(self, textvariable= self.dt_nasc_str, width=40)
        self.entrydt_nasc.grid(row=6, column=1)

        self.labelsalario= tk.Label(self, text='salario')
        self.labelsalario.grid(row=7)
        self.salario_str= tk.StringVar()
        self.entrysalario= tk.Entry(self, textvariable= self.salario_str, width=40)
        self.entrysalario.grid(row=7, column=1)

        self.labelcargo= tk.Label(self, text='cargo')
        self.labelcargo.grid(row=8)
        self.cargo_str= tk.StringVar()
        self.entrycargo= tk.Entry(self, textvariable= self.cargo_str, width=40)
        self.entrycargo.grid(row=8, column=1)

        self.labelemail= tk.Label(self, text='e-mail')
        self.labelemail.grid(row=9)
        self.email_str= tk.StringVar()
        self.entryemail= tk.Entry(self, textvariable= self.email_str, width=40)
        self.entryemail.grid(row=9, column=1)

        self.labelsenha = tk.Label(self, text='Senha')
        self.labelsenha.grid(row=10)
        self.senha_str = tk.StringVar()
        self.entrysenha = tk.Entry(self, textvariable=self.senha_str, width=40)
        self.entrysenha.grid(row=10, column=1)

        self.button1 = tk.Button(self, text='Salvar', height=1, width=15,command=self.acao)
        self.button1.grid(row=11, column=1)
        self.label_str= tk.StringVar()

    def acao(self):
        #self.controle = Controle()
        self.controle.cadastrar_funcionario(self.name_str.get(), self.cpf_str.get(), self.endereco_str.get(), self.telefone_str.get(),
                                           self.dt_nasc_str.get(), self.email_str.get(), self.cargo_str.get(), self.salario_str.get(), self.senha_str.get())

        self.controller.show_frame("Inicio_gerente")
        self.name_str.set('')
        self.cpf_str.set('')
        self.endereco_str.set('')
        self.telefone_str.set('')
        self.dt_nasc_str.set('')
        self.salario_str.set('')
        self.cargo_str.set('')
        self.email_str.set('')
        self.senha_str.set('')

class Atualizar_Funcionario(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()

        self.labelname= tk.Label(self, text='Nome')
        self.labelname.grid(row=1)
        self.name_str= tk.StringVar()
        self.entryname= tk.Entry(self, textvariable= self.name_str, width=40)
        self.entryname.grid(row=1, column=1)

        self.labelcpf= tk.Label(self, text='Cpf')
        self.labelcpf.grid(row=2)
        self.cpf_str= tk.StringVar()
        self.entrycpf= tk.Entry(self, textvariable= self.cpf_str, width=40)
        self.entrycpf.grid(row=2, column=1)

        self.labelendereco= tk.Label(self, text='Endereco')
        self.labelendereco.grid(row=3)
        self.endereco_str= tk.StringVar()
        self.entryendereco= tk.Entry(self, textvariable= self.endereco_str, width=40)
        self.entryendereco.grid(row=3, column=1)

        self.labeltelefone= tk.Label(self, text='Telefone')
        self.labeltelefone.grid(row=4)
        self.telefone_str= tk.StringVar()
        self.entrytelefone= tk.Entry(self, textvariable= self.telefone_str, width=40)
        self.entrytelefone.grid(row=4, column=1)

        self.labeldt_nasc= tk.Label(self, text='dt_nasc')
        self.labeldt_nasc.grid(row=5)
        self.dt_nasc_str= tk.StringVar()
        self.entrydt_nasc= tk.Entry(self, textvariable= self.dt_nasc_str, width=40)
        self.entrydt_nasc.grid(row=5, column=1)

        self.labelsalario= tk.Label(self, text='salario')
        self.labelsalario.grid(row=6)
        self.salario_str= tk.StringVar()
        self.entrysalario= tk.Entry(self, textvariable= self.salario_str, width=40)
        self.entrysalario.grid(row=6,column=1)

        self.labelcargo= tk.Label(self, text='cargo')
        self.labelcargo.grid(row=7)
        self.cargo_str= tk.StringVar()
        self.entrycargo= tk.Entry(self, textvariable= self.cargo_str, width=40)
        self.entrycargo.grid(row=7, column=1)

        self.labelemail= tk.Label(self, text='e-mail')
        self.labelemail.grid(row=8)
        self.email_str= tk.StringVar()
        self.entryemail= tk.Entry(self, textvariable= self.email_str, width=40)
        self.entryemail.grid(row=8, column=1)

        self.labelsenha = tk.Label(self, text='Senha')
        self.labelsenha.grid(row=9)
        self.senha_str = tk.StringVar()
        self.entrysenha = tk.Entry(self, textvariable=self.senha_str, width=40)
        self.entrysenha.grid(row=9,column=1)

        self.button1 = tk.Button(self, text='Atualizar', height=1, width=15,command=self.acao)
        self.button1.grid(row=10, column=1)
        self.label_str= tk.StringVar()

    def acao(self):
        #self.controle = Controle()
        self.controle.atualizar_funcionario(self.name_str.get(), self.cpf_str.get(), self.endereco_str.get(), self.telefone_str.get(),
                                            self.dt_nasc_str.get(), self.email_str.get(), self.cargo_str.get(), self.salario_str.get(), self.senha_str.get())

        self.controller.show_frame('Inicio_gerente')

        self.name_str.set('')
        self.cpf_str.set('')
        self.endereco_str.set('')
        self.telefone_str.set('')
        self.dt_nasc_str.set('')
        self.salario_str.set('')
        self.cargo_str.set('')
        self.email_str.set('')
        self.senha_str.set('')

class Recuperar_Funcionario(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        #self.controle = Controle()

        self.cpfText = tk.Label(self, text='Cpf: ')
        self.cpf_st = tk.StringVar()
        self.cpf_inpt = tk.Entry(self, textvariable = self.cpf_st)
        
        self.cpfText.grid(row=1)
        self.cpf_inpt.grid(row=1, column=1)
        
        
        self.b = tk.Button(self, text='OK', command=self.acao)
        self.b.grid(row=2, column=1)
        
        
        self.name_str= tk.StringVar()
        self.entryname= tk.Label(self, textvariable= self.name_str, width=50)
        self.entryname.grid(row=3, column=1)

        self.cpf_str= tk.StringVar()
        self.entrycpf= tk.Label(self, textvariable= self.cpf_str, width=50)
        self.entrycpf.grid(row=4,column=1)

        self.endereco_str= tk.StringVar()
        self.entryendereco= tk.Label(self, textvariable= self.endereco_str, width=50)
        self.entryendereco.grid(row=5,column=1)

      
        self.telefone_str= tk.StringVar()
        self.entrytelefone= tk.Label(self, textvariable= self.telefone_str, width=22)
        self.entrytelefone.grid(row=6,column=1)

      
        self.dt_nasc_str= tk.StringVar()
        self.entrydt_nasc= tk.Label(self, textvariable= self.dt_nasc_str, width=22)
        self.entrydt_nasc.grid(row=7,column=1)

     
        self.salario_str= tk.StringVar()
        self.entrysalario= tk.Label(self, textvariable= self.salario_str, width=22)
        self.entrysalario.grid(row=8,column=1)

     
        self.cargo_str= tk.StringVar()
        self.entrycargo= tk.Label(self, textvariable= self.cargo_str, width=22)
        self.entrycargo.grid(row=9,column=1)

      
        self.email_str= tk.StringVar()
        self.entryemail= tk.Label(self, textvariable= self.email_str, width=50)
        self.entryemail.grid(row=10,column=1)


    def acao(self):
        print 'String aki o ' + self.cpf_str.get()
        self.funcionario = self.controle.retornar_funcionario(self.cpf_st.get())

        self.name_str.set("Nome: " + self.funcionario.nome)
        self.cpf_str.set("CPF: "+self.funcionario.cpf)
        self.endereco_str.set("Endereco: "+self.funcionario.endereco)
        self.telefone_str.set("Telefone: "+self.funcionario.telefone)
        self.dt_nasc_str.set("Data de nascimento: "+self.funcionario.dt_nasc)
        self.email_str.set("Email: "+self.funcionario.email)
        self.cargo_str.set("Cargo: "+self.funcionario.cargo)
        self.salario_str.set("Salario: "+self.funcionario.salario)

class Deletar_Funcionario(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle

        #self.controle = Controle()

        #self.menu = Menu_(self.root, self)

        self.texto = tk.Label(self, text='Digite o Cpf do Funcionario')

        self.cpf = tk.Label(self, text='Cpf')
        self.cpf_str = tk.StringVar()
        self.cpf_input = tk.Entry(self, textvariable = self.cpf_str)

        self.texto.grid(row=1)
        self.cpf.grid(row=2, column=0)
        self.cpf_input.grid(row=2, column=1)
              
        self.b = tk.Button(self, text='Deletar dados do funcionario', command=self.acao)
        self.b.grid(row=3, column=1)
        
        
        
    def acao(self):
       
        self.controle.deletar_funcionario(self.cpf_str.get() )
        self.controller.show_frame("Inicio_gerente")


        
        

        
if __name__ == "__main__":
    janela = tk.Tk()
    app = SampleApp(janela)
    app.mainloop()
