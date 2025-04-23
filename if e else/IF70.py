# 70 - Verifique se um número é maior que 0 e múltiplo de 9.

num = int(input('Digite um número: '))
if num > 0 and num % 9 == 0:
    print('Maior que 0 e múltiplo de 9')
else:
    print('Não satisfaz a condição')
