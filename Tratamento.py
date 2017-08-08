class Tratamento:
	
	def __init__(self, nome, valor):
		self.nome = nome
		self.valor = valor

	def __str__(self):
                return "Tratamento: " + self.nome + "\tValor: " + str(self.valor)
