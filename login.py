#Classe login
class Login:
    
    def __init__ (self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
		
    def __str__(self):
        return "usuario: "+self.usuario+"\nsenha: "+self.senha
