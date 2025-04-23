# 71 - Verifique se um número é maior que 50, mas não é múltiplo de 5.

num = int(input('Digite um número: '))
if num > 50 and num % 5 != 0:
    print('Maior que 50 e não múltiplo de 5')
else:
    print('Não satisfaz a condição')
