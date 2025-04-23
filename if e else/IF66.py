# 66 - Verifique se um número é maior que 50 e divisível por 4.

num = int(input('Digite um número: '))
if num > 50 and num % 4 == 0:
    print('Maior que 50 e divisível por 4')
else:
    print('Não satisfaz a condição')
