# O restaurante a quilo Bem-Bão cobra R$
#  55,00 por cada quilo de refeição. Escreva um
#  algoritmo que leia o peso do prato montado pelo
#  cliente (em gramas) e imprima o valor a pagar.
#  Assuma que a balança já desconte o peso do
#  prato

prato = float(input("Informe o peso prato: "))

desc = 0.100

total = (prato - desc) * 55.00

print(f"O preço total será de: {total:.2f}R$")