# 65 - Verifique se a soma de três números é maior que 500.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
soma = a + b + c
if soma > 500:
    print('Soma maior que 500')
else:
    print('Soma não é maior que 500')
