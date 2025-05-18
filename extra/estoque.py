# Vamos às compras. Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque como valores. 
# Permita que o usuário insira um produto e verifique se ele está em estoque. Se estiver, informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.

estoque = {
    "maçã": 20,
    "banana": 35,
    "laranja": 12,
    "abacaxi": 5,
    "uva": 0
}

produto = input("Digite o nome do produto que deseja verificar: ").lower()

if produto in estoque:
    quantidade = estoque[produto]
    if quantidade > 0:
        print(f"Temos {quantidade} unidades de '{produto}' em estoque.")
    else:
        print(f"O produto '{produto}' está esgotado no momento.")
else:
    print(f"O produto '{produto}' não está disponível no estoque.")
