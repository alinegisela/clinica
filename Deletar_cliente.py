from Tkinter import *
from controle import Controle

class Deletar_cliente:

    def __init__(self, master):
        

        self.controle = Controle()

        self.texto = Label(janela, text='Digite o Cpf do cliente')

        self.cpf = Label(janela, text='Cpf')
        self.cpf_str = StringVar()
        self.cpf_input = Entry(janela, textvariable = self.cpf_str)

        self.texto.grid(row=1)
        self.cpf.grid(row=2, column=0)
        self.cpf_input.grid(row=2, column=1)
              
        self.b = Button(janela, text='Deletar todos os dados do cliente', command=self.acao)
        self.b.grid(row=3, column=1)
        
        
        
    def acao(self):
        print self.controle.listaClientes[0]
        self.controle.deletar_cliente(self.cpf_str.get() )
        print self.controle.listaClientes[0]  

janela = Tk()
p = Deletar_cliente(janela)
janela.title("Clinica Sinta-se Bem")
janela.geometry("500x400")
janela.configure(background='Beige') 
janela.mainloop()
