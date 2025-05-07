
print("Controle de estoque!")


while True:
    print
    estoque = {
        10: {"nome": "Caderno", "quantidade": 0},
        20: {"nome": "Caneta", "quantidade": 0},
        30: {"nome": "Lápis", "quantidade": 0},
        40: {"nome": "Borracha", "quantidade": 0},
        50: {"nome": "Régua", "quantidade": 0}
    }
    print("E = entrada no estoque \n S = Saída no estoue \n R = Relatorio \n X = sair")
    escolha = input("Escolha a opção que deseja:")
    if escolha == "E":
        
        