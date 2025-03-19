# Um motorista deseja colocar no seu tanque X
#  reais de gasolina.
#  Escreva um algoritmo para ler o preço do litro da
#  gasolina e o valor do pagamento, e exibir quantos
#  litros ele conseguiu colocar no tanque.


preco = float(input("Informe o preço da gasolina (L): "))
valor = float(input("Informe o valor que sera gasto: "))

X = valor/preco

print(f"Serão abastecidos {X:.2f} litros de gasolina")