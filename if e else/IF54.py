# 54 - Verifique se um número é menor que 100 e é par.

num = int(input('Digite um número: '))
if num < 100 and num % 2 == 0:
    print('Número é par e menor que 100')
else:
    print('Não satisfaz a condição')
