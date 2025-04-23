# 82 - Verifique se a multiplicação de dois números é ímpar.

a = int(input())
b = int(input())
if (a * b) % 2 != 0:
    print('Multiplicação é ímpar')
else:
    print('Multiplicação não é ímpar')
