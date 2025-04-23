# 49 - Verifique se um número é maior que 100 e múltiplo de 3.

num = int(input('Digite um número: '))
if num > 100 and num % 3 == 0:
    print('Maior que 100 e múltiplo de 3')
else:
    print('Não satisfaz a condição')
