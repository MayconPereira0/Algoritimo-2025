# 62 - Verifique se a média de dois números é menor que 30.

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
media = (a + b) / 2
if media < 30:
    print('Média menor que 30')
else:
    print('Média não é menor que 30')
