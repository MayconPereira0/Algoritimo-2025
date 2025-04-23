# 58 - Verifique se a soma de dois números é menor que 10 ou maior que 100.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b
if soma < 10 or soma > 100:
    print('Satisfaz a condição')
else:
    print('Não satisfaz a condição')
