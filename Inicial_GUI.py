from Tkinter import *
from controle import Controle

janela = Tk()

def cadastro_cliente():
    print 'chegou aqui'

def cadastro_tratamento():
    print 'chegou'
    
    
b1= Button(janela, width=20, text="Cadastrar Cliente", command=cadastro_cliente)
b1.place(x=10, y=30)

b2= Button(janela, width=30, text="Cadastrar Tratamento", command=cadastro_tratamento)
b2.place(x=200, y=30)

b1= Button(janela, width=20, text="Cadastrar Venda", command=cadastro_cliente)
b1.place(x=10, y=80)

b1= Button(janela, width=20, text="Pacotes mais lucrativos", command=cadastro_cliente)
b1.place(x=200, y=80)

b1= Button(janela, width=20, text="Lista de pacotes por cliente", command=cadastro_cliente)
b1.place(x=10, y=130)




janela.title("Clinica Sinta-se Bem")
janela.geometry("500x400")
janela.configure(background='Beige') 
janela.mainloop()
