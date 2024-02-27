""""
Menu SalesForce
"""
listaDeCadastro = []
listaCredenciais = []
servico1 = 0
servico2 = 0

print("Bem vindo a SalesForce"
      "\n"
      "\n1 - Cadastro"
      "\n2 - Login"
      "\n0 - Sair")

verf = int(input("\nDigite a opção desejada: "))

while (verf != 0):

    match verf:

        case 1:
            print("\nTela de Cadastro")
            nome = input("\nDigite seu nome completo: ")
            email = input("\nDigite seu e-mail: ")
            senha = input("\nDigite sua senha: ")
            cargo = input("\nDigite seu cargo: ")
            telefone = input("\nDigite seu telefone: ")
            nomeDaEmpresa = input("\nDigite a sua empresa: ")

            listaDeCadastro.append([nome, cargo , telefone , nomeDaEmpresa])
            listaCredenciais.append([email,senha])
            print("\n"
                  "\n1 - Cadastro"
                  "\n2 - Login"
                  "\n0 - Sair")

            verf = int(input("\nDigite a opção desejada: "))


        case 2:

            print("\nTela de login")
            verfEmail = input("\nEmail: ")
            verfSenha = input("\nSenha: ")

            while (verfEmail != email or verfSenha != senha):
                print("\nDados Incorretos, tente novamente!\n")

                verfEmail = input("\nEmail: ")
                verfSenha = input("\nSenha: ")

            print("\nLogin efetuado com sucesso!")
            break

        case 0:

            print("Volte sempre!")
            break

        case _:
            verf = int(input("\n1 - Cadastro"
                             "\n2 - Login"
                             "\n0 - Sair"
                             "\nFavor selecione uma opção válida: "))

def exibir_menu():
    return int(input("\n1 - Todos nossos serviços"
                  "\n2 - Assinar um serviço"
                  "\n3 - Listar meus serviços"
                  "\n4 - Histórico de pedidos"
                  "\n5 - Exibir meus dados"
                  "\n0 - Sair\n"
                  "\nDigite a opção desejada: "))

opcao = exibir_menu()

def historicoServico1():
    print("\n=============="
          "\nServiço:"
          "\nId: 1"
          "\nNome: IA Eistein"
          "\nValor: 15800.00"
          f"\nQuantidade de parcelas: {parcela1}"
          f"\nMetodo de pagamento: {metodo1}"
          f"\nValor das parcelas: {valorParcela1}")

def historicoServico2():
    print("\n=============="
          "\nServiço:"
          "\nId: 2"
          "\nNome: Sales"
          "\nValor: 23000.00"
          f"\nQuantidade de parcelas: {parcela2}"
          f"\nMetodo de pagamento: {metodo2}"
          f"\nValor das parcelas: {valorParcela2}")

def exibirServico1():
    print("\n=============="
          "\nServiço:"
          "\nId: 1"
          "\nNome: IA Eistein"
          "\nDescrição: Serviço de IA"
          "\nCategoria: IA"
          "\nValor: 15800.00")

def exibirServico2():
    print("\n=============="
          "\nServiço:"
          "\nId: 2"
          "\nNome: Sales"
          "\nDescrição: Serviço de Sales"
          "\nCategoria: Sales"
          "\nValor: 23000.00")

while (opcao != 0):

    match (opcao):

        case 1:

            print("\n=============="
                  "\nServiço:"
                  "\nId: 1"
                  "\nNome: IA Eistein"
                  "\nDescrição: Serviço de IA"
                  "\nCategoria: IA"
                  "\nValor: 15800.00"
                  "\n=============="
                  "\nServiço:"
                  "\nId: 2"
                  "\nNome: Sales"
                  "\nDescrição: Serviço de Sales"
                  "\nCategoria: Sales"
                  "\nValor: 23000.00")

            opcao = exibir_menu()


        case 2:

            assinatura = int(input("Digite o serviço que deseja assinar: "))

            if (assinatura == 1 and servico1 == 0):
                parcela1 = int(input("Digite a quantidade de parcelas: "))
                metodo1 = input("Digite o método do pagamento: ")
                valorParcela1 = 15800.00/parcela1
                print("Serviço 'IA Eistein' assinado")
                servico1 += 1
            elif (assinatura == 2 and servico2 == 0):
                parcela2 = int(input("Digite a quantidade de parcelas: "))
                metodo2 = input("Digite o método do pagamento: ")
                valorParcela2 = 23000.00 / parcela2
                print("Serviço 'Sales' assinado")
                servico2 += 1
            elif (servico1 == 1 or servico2 == 1):
                print("Serviço já assinado")
            else:
                assinatura = input("Informe uma opção válida: ")

            opcao = exibir_menu()

        case 3:

            if (servico1 == 1 and servico2 == 1):
                exibirServico1()
                exibirServico2()
            elif(servico1 == 1):
                exibirServico1()
            elif(servico2 == 2):
                exibirServico2()
            else:
                print("\nInfelizmente ainda não há serviços contratados")

            opcao = exibir_menu()

        case 4:

            if (servico1 == 1 and servico2 == 1):
                historicoServico1()
                historicoServico2()
            elif (servico1 == 1):
                historicoServico1()
            elif (servico2 == 2):
                historicoServico2()
            else:
                print("\nNão há histórico de compras a ser exibido")

            opcao = exibir_menu()

        case 5:

            print("Segue os dados cadastrados, favor considerar respectivamente: "
                  "\nNome, Cargo , Telefone e Nome da Empresa")
            for informacoes in listaDeCadastro:
                print(informacoes)
            print("Email e senha:")
            for credenciais in listaCredenciais:
                print(credenciais)

            opcao = exibir_menu()


        case 0:

            break

        case _:

            print("Opção inválida!")

            opcao = exibir_menu()


print("\nObrigado por usar a Salesforce!")