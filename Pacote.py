class Pacote:
	
	def __init__(self, id, total, tratamentos):
                #id random
		self.id = id
		self.total = total
		self.tratamentos = tratamentos
		self.lucro = 0.6 * float(total)

        #salva todos os __str__ dos tratamentos
	def retornarTratamentos(self):
                tratamentos = ""
                for i in range(len(self.tratamentos)):
                        tratamentos += str(i+1) + " - " + self.tratamentos[i].__str__() + "\n"
                return tratamentos
        
	def __str__(self):
                tratamentos = self.retornarTratamentos()
               
                return "Valor total do pacote: " + str(self.total)+"\nLucro para a empresa: " + str(self.lucro)+ "\n\n" + tratamentos
