from datetime import date
class Funcionario:
	
	def __init__(self, nome, cpf, endereco, telefone, dt_nasc, email, cargo, salario):
	
                self.nome = nome
		self.cpf = cpf
		self.endereco = endereco
		self.telefone = telefone
		self.dt_nasc = dt_nasc
		self.email = email
		self.cargo = cargo
		self.salario = salario

        def __str__(self):
                return "Nome: " + self.nome + "\nCPF: " + self.cpf +"\nEndereco: " + self.endereco + "\nTelefone: " + self.telefone +"\nData de nascimento: " + self.dt_nasc.strftime('%d/%m/%Y') + "\nEmail: " + self.email +"\nCargo: " + self.cargo + "\nSalario: " + self.salario
