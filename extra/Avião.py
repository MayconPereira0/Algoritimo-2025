# 1 – Exercício de Tratamento de Exceção:

# Crie um software de venda de passagem aérea, que terá os seguintes dados de cadastro:
# Cadastro Cliente:
# Nome
# Sobrenome
# Rg
# CPF
# Endereço
# Fone
# Idade
# Cadastro Passagem:
# Destino
# Origem
# Duração
# Valor Passagem
# Desconto (5%)
# Cadastro Avião:
# Modelo
# Ano
# Horas de Voo
# Cor
# Quantidade de passageiros
# Cadastro Tripulação:
# Nome
# Descrição Cargo
# Idade
# Data de Admissão
# Fone

clientes = []
passagens = []
avioes = []
tripulacao = []

def cadastrar_cliente():
    try:
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        rg = input("RG: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        idade = int(input("Idade: "))

        cliente = {
            "nome": nome,
            "sobrenome": sobrenome,
            "rg": rg,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": telefone,
            "idade": idade
        }

        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar cliente:", erro)

def cadastrar_passagem():
    try:
        print("\n--- Cadastro de Passagem ---")
        origem = input("Origem: ")
        destino = input("Destino: ")
        duracao = input("Duração (ex: 2h30): ")
        valor = float(input("Valor da passagem: R$ "))
        desconto = valor * 0.05
        valor_final = valor - desconto

        passagem = {
            "origem": origem,
            "destino": destino,
            "duracao": duracao,
            "valor": valor,
            "desconto": desconto,
            "valor_final": valor_final
        }

        passagens.append(passagem)
        print("Passagem cadastrada com sucesso!")

    except ValueError:
        print("Digite um valor válido para o preço da passagem.")
    except Exception as erro:
        print("Erro ao cadastrar passagem:", erro)

def cadastrar_aviao():
    try:
        print("\n--- Cadastro de Avião ---")
        modelo = input("Modelo do avião: ")
        ano = int(input("Ano: "))
        horas_voo = float(input("Horas de voo: "))
        cor = input("Cor: ")
        capacidade = int(input("Quantidade de passageiros: "))

        aviao = {
            "modelo": modelo,
            "ano": ano,
            "horas_voo": horas_voo,
            "cor": cor,
            "capacidade": capacidade
        }

        avioes.append(aviao)
        print("Avião cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar avião:", erro)

def cadastrar_tripulacao():
    try:
        print("\n--- Cadastro da Tripulação ---")
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        idade = int(input("Idade: "))
        data_admissao = input("Data de admissão (dd/mm/aaaa): ")
        telefone = input("Telefone: ")

        tripulante = {
            "nome": nome,
            "cargo": cargo,
            "idade": idade,
            "data_admissao": data_admissao,
            "telefone": telefone
        }

        tripulacao.append(tripulante)
        print("Tripulante cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar tripulante:", erro)

def mostrar_relatorios():
    print("\n--- Relatórios ---")

    print("\nClientes:")
    for cliente in clientes:
        print(cliente)

    print("\nPassagens:")
    for passagem in passagens:
        print(passagem)

    print("\nAviões:")
    for aviao in avioes:
        print(aviao)

    print("\nTripulação:")
    for membro in tripulacao:
        print(membro)

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Passagem")
        print("3 - Cadastrar Avião")
        print("4 - Cadastrar Tripulação")
        print("5 - Ver Relatórios")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_cliente()
            elif opcao == 2:
                cadastrar_passagem()
            elif opcao == 3:
                cadastrar_aviao()
            elif opcao == 4:
                cadastrar_tripulacao()
            elif opcao == 5:
                mostrar_relatorios()
            elif opcao == 6:
                print("Encerrando o sistema... Até mais!")
                break
            else:
                print("Opção inválida! Digite de 1 a 6.")
        except ValueError:
            print("Digite um número válido.")
        except Exception as erro:
            print("Erro inesperado:", erro)

menu()

