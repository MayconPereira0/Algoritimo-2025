# 61 - Verifique se a média de dois números é maior que 50.

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
media = (a + b) / 2
if media > 50:
    print('Média maior que 50')
else:
    print('Média não é maior que 50')
