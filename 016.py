# Faça um algoritmo que receba um valor que
#  foi depositado e exiba o valor com rendimento
#  após um mês.- Considere fixo os juros de poupança 0,70% a.m

valor = float(input("Digite um valor: "))

rendi = valor + valor * 0.007

print(f"{rendi:.2f}")