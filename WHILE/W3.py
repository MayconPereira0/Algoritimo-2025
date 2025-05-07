


while True:
    
    print("\n1-Ver saldo \n2-Depositar \n3-Sacar \n4-Cadastrar \n5-Sair")

    escolha = input("escolha a opção para proseguir: ")

    if escolha == "4":

        clientes = []

        dados_clie={}

        dados_clie["nome"] = input("Digite seu nome completo: ")
        dados_clie["CPF"] = input("Digite seu CPF: ")
        dados_clie["RG"] = input("Digite o N° do seu RG: ")
        dados_clie["tel"] = input("Digite seu telefone: ")
        dados_clie["agen"] = input("Digite a agencia do seu banco: ")
        dados_clie["conta"] = input("Digite o N° da conta: ")
        dados_clie["saldo"] = int(input("Digite o valor que deseja depositar: ")) 

        clientes.append(dados_clie)

    if escolha == "1":
        print(f"{dados_clie["saldo"]:.2f}")

    elif escolha == "2":
        deposita = float(input("Digite o valor que deseja inserir:"))
        dados_clie["saldo"]+=deposita

    elif escolha == "3":
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        dados_clie["saldo"]-=valor_saque

    elif escolha == "5":
        break



