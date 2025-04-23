# Verifique se a média de três números é menor que 20.

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
media = (a + b + c) / 3
if media < 20:
    print('A média é menor que 20.')
else:
    print('A média não é menor que 20.')