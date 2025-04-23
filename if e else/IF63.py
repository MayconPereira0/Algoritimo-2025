# 63 - Verifique se a multiplicação de dois números é maior que 500.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
produto = a * b
if produto > 500:
    print('Produto maior que 500')
else:
    print('Produto não é maior que 500')
