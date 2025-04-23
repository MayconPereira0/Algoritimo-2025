# 56 - Verifique se um número é positivo e múltiplo de 3, mas não de 5.

num = int(input('Digite um número: '))
if num > 0 and num % 3 == 0 and num % 5 != 0:
    print('Satisfaz a condição')
else:
    print('Não satisfaz a condição')
