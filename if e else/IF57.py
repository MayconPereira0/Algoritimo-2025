# 57 - Verifique se a soma de dois números é igual a 20 ou maior que 50.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b
if soma == 20 or soma > 50:
    print('Satisfaz a condição')
else:
    print('Não satisfaz a condição')
