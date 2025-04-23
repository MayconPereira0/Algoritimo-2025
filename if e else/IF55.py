# 55 - Verifique se um número é negativo e divisível por 5.

num = int(input('Digite um número: '))
if num < 0 and num % 5 == 0:
    print('Número é negativo e divisível por 5')
else:
    print('Não satisfaz a condição')
