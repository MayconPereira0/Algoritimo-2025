# 69 - Verifique se um número é maior que 50 e divisível por 3.

num = int(input('Digite um número: '))
if num > 50 and num % 3 == 0:
    print('Maior que 50 e divisível por 3')
else:
    print('Não satisfaz a condição')
