#Classe teste
from controle import Controle

class Teste:
    controle = Controle()
    
    opcao = int(raw_input('Escolha uma opção:\n'
                '1. Cadastrar Cliente\n'
                '2. Cadastrar tratamento\n'
                '3. Cadastrar Pacote\n'
                '4. Realizar venda a um cliente\n'
                '5. listar pacotes maior lucro\n'
                '6. lista pacotes para por cliente'))

            
    while(opcao > 0 and opcao < 8):

                if opcao == 1:
                    nome = raw_input('Nome')
                    cpf = raw_input('cpf')
                    endereco = raw_input('End')
                    telefone = raw_input('Tel')
                    email = raw_input('email')
                    
                    controle.cadastrar_cliente(nome, cpf, endereco, telefone, email)

                elif opcao == 2:
                    nome = raw_input('Nome')
                    valor = raw_input('valor')

                    controle.cadastrar_tratamento(nome, valor)

                elif opcao == 3:
                    

                    controle.cadastrar_pacote()
                    
                elif opcao == 7:
                    lista = controle.listaClientes
                    nova_lista = []
                    for i in range(len(lista)):
                        nova_lista.append(lista[i].__str__())
                    print nova_lista
                        



                opcao = int(raw_input('Escolha uma opção:\n'
                    '1. Cadastrar Cliente\n'
                    '2. Cadastrar tratamento\n'
                    '3. Cadastrar Pacote\n'
                    '4. Realizar venda a um cliente\n'
                    '5. listar pacotes maior lucro\n'
                    '6. lista pacotes para por cliente'
                    '7. lista clientes'))
