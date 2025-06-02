# Crie um programa em Python que cadastre usuários com nome e idade, sexo, CPF, Endereço, Cidade e Estado, armazenando esses dados em listas e, ao final, salve todas as informações em um arquivo cadastro.txt.
# O Aplicativo deverá ter um módulo de consulta de todos os dados.
# Regras:

# Cadastro:
# O usuário pode cadastrar quantas pessoas quiser.
# O programa deve perguntar ao final de cada cadastro se deseja cadastrar outra pessoa.
# Use try e except para garantir valores válidos.
# Após encerrar os cadastros, grave os dados no arquivo cadastro.txt, no formato:
# Consultas:
# O usuário deverá consultar somente uma linha e retornar apenas o que foi solicitado.

# Sair
# Ao definir sair, o programa será encerrado e os dados preservados.


# Ex.
# Nome: Maria, Idade: 22, Sexo:F, Endereço: Rua Afonso Penas, 4995, Cidade: Campo Grande, Estado: MS
# -------------------------------------------------------------------------------------------------- 
# Nome: João, Idade: 30, Sexo:M, Endereço: Rua Afonso Penas, 4996, Cidade: Campo Grande, Estado: MS

nomes = []
idades = []
sexos = []
cpfs = []
enderecos = []
cidades = []
estados = []

def cadastrar_usuario():
    try:
        nome = input("Digite o nome: ").strip()
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        while sexo not in ['M', 'F']:
            print("Sexo inválido! Use M ou F.")
            sexo = input("Digite o sexo (M/F): ").strip().upper()
        cpf = input("Digite o CPF: ").strip()
        endereco = input("Digite o endereço (Rua, número): ").strip()
        cidade = input("Digite a cidade: ").strip()
        estado = input("Digite o estado (sigla): ").strip().upper()

        # Adiciona aos dados
        nomes.append(nome)
        idades.append(idade)
        sexos.append(sexo)
        cpfs.append(cpf)
        enderecos.append(endereco)
        cidades.append(cidade)
        estados.append(estado)
        print("Cadastro realizado com sucesso!\n")
    except ValueError:
        print("Erro: idade deve ser um número inteiro!\n")

def salvar_dados():
    with open("extra/cadastro.txt", "w", encoding="utf-8") as f:
        for i in range(len(nomes)):
            f.write(f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo:{sexos[i]}, "
                    f"CPF: {cpfs[i]}, Endereço: {enderecos[i]}, "
                    f"Cidade: {cidades[i]}, Estado: {estados[i]}\n")
            f.write("--------------------------------------------------------------------------------------------------\n")
    print("Dados salvos em 'cadastro.txt'.\n")

def consultar_dado():
    nome_busca = input("Digite o nome que deseja consultar: ").strip()
    encontrado = False
    for i in range(len(nomes)):
        if nomes[i].lower() == nome_busca.lower():
            print(f"\nNome: {nomes[i]}")
            print(f"Idade: {idades[i]}")
            print(f"Sexo: {sexos[i]}")
            print(f"CPF: {cpfs[i]}")
            print(f"Endereço: {enderecos[i]}")
            print(f"Cidade: {cidades[i]}")
            print(f"Estado: {estados[i]}")
            encontrado = True
            break
    if not encontrado:
        print("Usuário não encontrado.\n")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar novo usuário")
        print("2. Consultar dados")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            while True:
                cadastrar_usuario()
                continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
                if continuar != 'S':
                    break
        elif opcao == '2':
            consultar_dado()
        elif opcao == '3':
            salvar_dados()
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()
