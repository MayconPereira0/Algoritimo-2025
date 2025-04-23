# Verifique se a média de três números é maior que 50.

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
media = (a + b + c) / 3
if media > 50:
    print('A média é maior que 50.')
else:
    print('A média não é maior que 50.')