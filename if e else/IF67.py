# 67 - Verifique se um número é divisível por 6 e maior que 100.

num = int(input('Digite um número: '))
if num % 6 == 0 and num > 100:
    print('Divisível por 6 e maior que 100')
else:
    print('Não satisfaz a condição')
