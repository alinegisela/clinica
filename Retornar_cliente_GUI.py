from Tkinter import *
from controle import Controle
from Menu_GUI import Menu_

class Retornar_cliente:

    def __init__(self, master, cpf):
       

        self.menu = Menu_(master)

        self.controle = Controle()
        self.cliente = self.controle.retornar_cliente(cpf)

        self.nome = Label(janela, text="Nome: ")
        self.nome_input = Label(janela, text=self.cliente.nome)

        self.cpf = Label(janela, text='Cpf: ')
        self.cpf_input = Label(janela, text = self.cliente.cpf)


        self.endereco = Label(janela, text='Endereço: ')
        self.endereco_input = Label(janela, text = self.cliente.endereco)
    
        self.telefone = Label(janela, text='Telefone')
        self.telefone_input = Label(janela, text = self.cliente.telefone)

        self.email = Label(janela, text='Email')
        self.email_input = Label(janela, text = self.cliente.email)

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
        self.b2 = Button(janela, text='Deletar dados do cliente', command=self.acao)
        self.b.grid(row=6, column=1)
        
        
        
    def acao(self):
        self.controle.retornar_cliente(self.cpf_str.get())
      

janela = Tk()
p = Retornar_cliente(janela, 'a')
janela.title("Clinica Sinta-se Bem")
janela.geometry("500x400")
janela.configure(background='Beige') 
janela.mainloop()
