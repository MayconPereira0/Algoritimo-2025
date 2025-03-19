#  Um funcionário recebe um salário fixo mais
#  4% decomissão sobre as vendas.
#  Faça um algoritmo que receba o salário fixo de
#  um funcionário e o valor de suas vendas, calcule
#  e mostre o salário sem a comissão, o valor da
#  comissão e o salário final do funcionário.

fixo = float(input("Informe o salário fixo: "))

vendas = float(input("Informe o valor das vendas: "))

comis = vendas * 0.04

total = fixo + comis

print(f"O salário fico é de: {fixo:.2f}R$, o valor da comissão: {comis:.2f}R$, o valor total: {total:.2f} ")

