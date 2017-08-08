# Classe Cliente

class Cliente:

    def __init__(self, nome, cpf, endereco, telefone, email):

        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def __str__ (self):
        return 'Nome: '+self.nome+' cpf: '+self.cpf+' endereco: '+self.endereco+' fone: '+self.telefone+' email: '+self.email

    
