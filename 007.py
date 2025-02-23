#  Valores de uma Compra– Um cliente de uma
#  loja está comprando cinco produtos.
#  Crie um algoritmo que solicite o preço de cada
#  um desses produtos e, em seguida, exiba o
#  subtotal da venda, o valor do imposto e o valor
#  total (subtotal da venda mais o valor do imposto).
#  Suponha que a alíquota do imposto seja de 6%
#  sobre o subtotal da venda.

quant = int(input("Informe a quantidade de produtos: "))

i = 1
produtos = []

while i <= quant:
    soma = float(input(f"Informe o produto {i}: "))
    produtos.append(soma)
    i += 1

sub = (sum(produtos))

imp = (sub * 0.06)

print(f"\n{" "*12}Nota fiscal{" "*12} \n {produtos} \n imposto:{"-"*22}{imp:.2f} \n O subtotal:{"-"*19}{sum(produtos):.2f} \n Total:{"-"*24}{sub + imp:.2f} ")
