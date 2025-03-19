# Faça um programa que leia o nome de um 
# produto, a quantidade comprada, o valor unitário 
# e o percentual de desconto a ser aplicado para o
# pagamento. 
# Imprima na tela o nome do produto e o valor total 
# da venda.


nome = (input("Digite o nome do produto = "))
qtde = int(input("Digite a quantidade de produtos = "))
valor = float(input("Digite o valor unitário = "))
desc = float(input("Digite o valor do desconto(%) = "))
total = float(valor-(valor*desc/100))
print("\nNome = ", nome)
print("Quantidade = ", qtde)
print("Valor Unitário = R$ ", valor)
print("Desconto = ", desc, "%")
print("Valor Total = R$ ", total)
