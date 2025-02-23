# Faça um algoritmo para ler o salário bruto de
#  um funcionário e aumentá-lo em 15%.
#  Após o aumento, desconte 8% de impostos.
#  Imprima o salário inicial, o salário com o aumento
#  sem descontar o imposto, o valor do imposto e o
#  salário final

sal = int(input("Informe o salário bruto: "))

aumento = (sal * 0.15) + sal

imposto = 0.08

final = aumento - imposto

print(f"\n salário inicial: {sal} \n aumento: {aumento} \n Imposto: 8% \n O salário final será de: {final}")