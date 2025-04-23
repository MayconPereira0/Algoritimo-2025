# 64 - Verifique se a multiplicação de dois números é menor que 1000.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
produto = a * b
if produto < 1000:
    print('Produto menor que 1000')
else:
    print('Produto não é menor que 1000')
