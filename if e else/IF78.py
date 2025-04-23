# 78 - Verifique se a soma de três números é maior que 100 e menor que 200.

a = int(input())
b = int(input())
c = int(input())
soma = a + b + c
if 100 < soma < 200:
    print('Soma entre 100 e 200')
else:
    print('Fora da faixa')
