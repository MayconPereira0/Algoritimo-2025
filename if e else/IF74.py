# 74 - Verifique se a média de três números é maior que 40.

a = float(input())
b = float(input())
c = float(input())
media = (a + b + c) / 3
if media > 40:
    print('Média maior que 40')
else:
    print('Média não é maior que 40')
