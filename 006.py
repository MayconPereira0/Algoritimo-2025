# Previsão de vendas– Sabendo que o lucro
#  anual de uma empresa é, tipicamente, 23% do
#  total de vendas, crie um algoritmo que solicite ao
#  usuário que entre com o valor projetado do total
#  de vendas no ano, em seguida, calcule e exiba o
#  lucro que deve ser obtido com esse valor, o valor
#  total (lucro+vendas) e apenas p valor das vendas.

vendas = float(input("Informe o total de vendas no ano: "))

lucro = (vendas * 0.23)

print(f"A margem de lucro do total de vendas: {vendas + lucro}, será: {lucro:.2f}")
