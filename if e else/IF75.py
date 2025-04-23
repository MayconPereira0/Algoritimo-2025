# 75 - Verifique se a média de três números é menor que 25.

a = float(input())
b = float(input())
c = float(input())
media = (a + b + c) / 3
if media < 25:
    print('Média menor que 25')
else:
    print('Média não é menor que 25')
