from Tkinter import *
from controle import Controle

janela = Tk()

def cadastro_cliente():
    print 'chegou aqui'
    
controle = Controle()
nome = Label(janela, text='Nome')
nome_input = Entry(janela)
cpf = Label(janela, text='Cpf')
cpf_input = Entry(janela)
endereco = Label(janela, text='Endereco')
endereco_input = Entry(janela)
telefone = Label(janela, text='Telefone')
telefone_input = Entry(janela)
email = Label(janela, text='Email')
email_input = Entry(janela)

nome.grid(row=1)
nome_input.grid(row=1, column=1)
cpf.grid(row=2)
cpf_input.grid(row=2, column=1)
endereco.grid(row=3)
endereco_input.grid(row=3, column=1)
telefone.grid(row=4)
telefone_input.grid(row=4, column=1)
email.grid(row=5)
email_input.grid(row=5, column=1)


print type(nome_input)
print type(str(nome_input))

b = Button(janela, text='aaa', command=controle.cadastrar_cliente)
b.grid(row=6)


b1= Button(janela, width=20, text="Lista de pacotes por cliente", command=cadastro_cliente)
b1.place(x=10, y=130)




janela.title("Clinica Sinta-se Bem")
janela.geometry("500x400")
janela.configure(background='Beige') 
janela.mainloop()
