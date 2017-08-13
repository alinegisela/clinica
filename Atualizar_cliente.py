from Tkinter import *
from controle import Controle

class Atualizar_cliente:

    def __init__(self, master):
        

        self.controle = Controle()

        self.nome = Label(janela, text='Nome')
        self.nome_str = StringVar()
        self.nome_input = Entry(janela, textvariable = self.nome_str)

        self.cpf = Label(janela, text='Cpf')
        self.cpf_str = StringVar()
        self.cpf_input = Entry(janela, textvariable = self.cpf_str)

        self.endereco = Label(janela, text='Endereco')
        self.endereco_str = StringVar()
        self.endereco_input = Entry(janela, textvariable = self.endereco_str)
    
        self.telefone = Label(janela, text='Telefone')
        self.telefone_str = StringVar()
        self.telefone_input = Entry(janela, textvariable = self.telefone_str)

        self.email = Label(janela, text='Email')
        self.email_str = StringVar()
        self.email_input = Entry(janela, textvariable = self.email_str)

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
        
        
        self.b = Button(janela, text='Atualizar dados do cliente', command=self.acao)
        self.b.grid(row=6, column=1)
        
        
        
    def acao(self):
        print self.controle.listaClientes[0]
        self.controle.atualizar_cliente(self.nome_str.get(), self.cpf_str.get(), self.endereco_str.get(), self.telefone_str.get(), self.email_str.get() )
        print self.controle.listaClientes[0]  

janela = Tk()
p = Atualizar_cliente(janela)
janela.title("Clinica Sinta-se Bem")
janela.geometry("500x400")
janela.configure(background='Beige') 
janela.mainloop()
