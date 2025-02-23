# A loja Mamão com açucar está vendendo
#  seus produtos em 5 (cinco) prestações sem juros.
#  Faça um algoritmo que receba um valor de uma
#  compra e mostre o valor das prestações.

compra = float(input("Digite o valor da compra: "))

prest = compra / 5

print(f"As prestções da compra ficarão: {prest:.2f}")