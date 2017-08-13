from Tkinter import *
from controle import *

class Menu_:
  
    
    def theend():
        global janela
        janela.destroy()

   

    #MENU
    
    def __init__(self, master):
      
        self.menu = Menu(master)
        master.config(menu=self.menu)
        master.title('')

        subMenu = Menu(self.menu)
    
        self.menu.add_cascade(label='Cliente', menu=subMenu)
        subMenu.add_command(label='Novo projeto')
        subMenu.add_command(label='Editar projeto')
        subMenu.add_separator()
        subMenu.add_command(label='Sair',command=self.theend)



