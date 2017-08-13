import Tkinter as tk
from controle import Controle

class SampleApp(tk.Frame):

    def __init__(self,janela ,*args, **kwargs):
        tk.Frame.__init__(self,janela, *args, **kwargs)
        self.root  = janela

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
        for F in (Cadastrar_cliente, StartPage, Atualizar_cliente, Retornar_cliente, Deletar_cliente, Login):
            page_name = F.__name__
            frame = F(parent=container, controller=self, root=self.root)
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

class StartPage(tk.Frame):

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        
        
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

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        self.controle = Controle()

        

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


class Login(tk.Frame):

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        self.controle = Controle()

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
        if validar == True:
            self.controller.show_frame("StartPage")

class Atualizar_cliente(tk.Frame):

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        self.controle = Controle()

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

global cpf
cpf = 'a'
class Retornar_cliente(tk.Frame):

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        
        self.menu = Menu_(self.root, self.controller)

        self.controle = Controle()
        self.cliente = self.controle.retornar_cliente( cpf)

        self.nome = tk.Label(self, text="Nome: ")
        self.nome_input = tk.Label(self, text=self.cliente.nome)

        self.cpf = tk.Label(self, text='Cpf: ')
        self.cpf_input = tk.Label(self, text = self.cliente.cpf)


        self.endereco = tk.Label(self, text='Endereco: ')
        self.endereco_input = tk.Label(self, text = self.cliente.endereco)
    
        self.telefone = tk.Label(self, text='Telefone')
        self.telefone_input = tk.Label(self, text = self.cliente.telefone)

        self.email = tk.Label(self, text='Email')
        self.email_input = tk.Label(self, text = self.cliente.email)

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
        
        #alterar os commands
        self.b = tk.Button(self, text='Atualizar dados do cliente', command=self.acao)
        self.b.grid(row=6, column=1)
        self.b2 = tk.Button(self, text='Deletar dados do cliente', command=self.acao)
        self.b.grid(row=6, column=0)
        
        
        
    def acao(self):
        self.controle.retornar_cliente(self.cpf_input.get())

class Deletar_cliente(tk.Frame):

    def __init__(self, parent, controller, root):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.root = root

        self.controle = Controle()

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
    
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Novo projeto', command=lambda : controller.show_frame("Cadastrar_cliente"))
        subMenu.add_command(label='Editar projeto')
        subMenu.add_separator()
        subMenu.add_command(label='Sair',command=self.theend)

    def remove(self):
        empty = tk.Menu(master)

    def mudar_pag(self, nome_pag, master):
        g.nome_pag(master, "Cadastrar_cliente")
if __name__ == "__main__":
    janela = tk.Tk()
    app = SampleApp(janela)
    app.mainloop()
