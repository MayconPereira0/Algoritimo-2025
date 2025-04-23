# 68 - Verifique se um número é menor que 10 e divisível por 5.

num = int(input('Digite um número: '))
if num < 10 and num % 5 == 0:
    print('Menor que 10 e divisível por 5')
else:
    print('Não satisfaz a condição')
