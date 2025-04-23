# 50 - Verifique se a soma de dois números é menor que 20 e maior que 10.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b
if 10 < soma < 20:
    print('A soma está entre 10 e 20')
else:
    print('A soma não está entre 10 e 20')
