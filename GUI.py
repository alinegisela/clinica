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
        container.pack(side="top",  expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        janela.title("Clinica Sinta-se Bem")
        janela.geometry("500x400")
        #janela.configure(backgr.grid_bg='Beige'
        #self.menu = Menu_(self.root, self)

        self.frames = {}
        for F in (Cadastrar_cliente, StartPage, Atualizar_cliente, Retornar_cliente, Deletar_cliente, Login, Inicio, Cadastrar_venda, Recuperar_pacotes, Inicio_gerente, Cadastrar_pacote, Deletar_pacote):
            page_name = F.__name__
            frame = F(parent=container, controller=self, root=self.root, controle=self.controle)
            self.frames[page_name] = frame
           

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

      
        self.show_frame("Login")
        
  

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()
    def menu_gerente(self, page_name):
        frame = self.frames[page_name]
        frame.updateGerente()
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller, root, controle):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        self.controle = controle
        
        
        label = tk.Label(self, text="Teste")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Mostrar cliente",
                            command=lambda: controller.show_frame("Deletar_cliente"))
        button2 = tk.Button(self, text="Cadastrar cliente",
                            command=lambda: controller.show_frame("Atualizar_cliente"))
        button1.pack()
        button2.pack()

    def update(self):
        self.menu = Menu_(self.root, self.controller)

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
        #self.menu = Menu_(self.root, self)

        self.usuario = tk.Label(self, text='Usuario: ')
        self.usuario_str = tk.StringVar()
        self.usuario_input = tk.Entry(self, textvariable = self.usuario_str)

        self.senha = tk.Label(self, text='Senha: ')
        self.senha_str = tk.StringVar()
        self.senha_input = tk.Entry(self, textvariable = self.senha_str)


        self.usuario.grid(row=1)
        self.usuario_input.grid(row=1, column=1)
        self.senha.grid(row=2)
        self.senha_input.grid(row=2, column=1)
        
        
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
        

        self.cpfText.grid(row=0)
        self.cpf_inpt.grid(row=0, column=1)
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
        subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Cadastrar novo cliente', command=lambda : controller.show_frame("Cadastrar_cliente"))
        subMenu.add_command(label='Atualizar dados de um cliente', command=lambda : controller.show_frame("Atualizar_cliente"))
        subMenu.add_command(label='Buscar um cliente', command=lambda : controller.show_frame("Retornar_cliente"))
    

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

        for i in range(len(self.controle.listar_pacotes_lucro())):
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

    def update(self):
        print 'update'
        self.pacotes.set(self.controle.listar_pacotes())
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


        for i in range(len(self.controle.listar_pacotes_lucro())):
            self.lb.insert(i+1, "Pacote "+str(i+1))

      
        self.lb.grid()

        self.b = tk.Button(self, text='Deletar pacote(s)', command=self.acao)
        self.b.grid(row=3, column=1)
        
        self.pacotes = tk.StringVar()
        
       
        self.nome = tk.Label(self, textvariable=self.pacotes)
        
        self.nome.grid(row=2)
        
        
    def acao(self):
       
      

        lista = self.lb.curselection()
        trat_selec = []
        
        for i in range(len(lista)):
            trat_selec.append(lista[i])
            
        self.controle.deletar_pacote(trat_selec)
        self.controller.show_frame("Inicio")
        
    def update(self):
        print 'update'
        self.pacotes.set(self.controle.listar_pacotes())
        

  
    
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

        subMenu2 = tk.Menu(self.menu)

        self.menu.add_cascade(label='Pacotes', menu=subMenu2)
        subMenu2.add_command(label='Cadastrar novo pacote', command=lambda : controller.show_frame("Cadastrar_pacote"))
        subMenu2.add_command(label='Excluir pacote', command=lambda : controller.show_frame("Deletar_pacote"))

        subMenu3 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Vendas', menu=subMenu3)
        subMenu3.add_command(label='Registrar nova venda', command=lambda : controller.show_frame("Cadastrar_venda"))
        
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

        subMenu2 = tk.Menu(self.menu)

        self.menu.add_cascade(label='Pacotes', menu=subMenu2)
        subMenu2.add_command(label='Cadastrar novo pacote', command=lambda : controller.show_frame("Cadastrar_pacote"))
        subMenu2.add_command(label='Excluir pacote', command=lambda : controller.show_frame("Deletar_pacote"))

        subMenu3 = tk.Menu(self.menu)
        self.menu.add_cascade(label='Vendas', menu=subMenu3)
        subMenu3.add_command(label='Registrar nova venda', command=lambda : controller.show_frame("Cadastrar_venda"))
        
        
        subMenu.add_separator()
        subMenu.add_command(label='Sair',command=self.theend)


if __name__ == "__main__":
    janela = tk.Tk()
    app = SampleApp(janela)
    app.mainloop()
