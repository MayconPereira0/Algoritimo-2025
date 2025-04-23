# 48 - Verifique se um número é múltiplo de 2 e 5.

num = int(input('Digite um número: '))
if num % 2 == 0 and num % 5 == 0:
    print('Múltiplo de 2 e 5')
else:
    print('Não é múltiplo de 2 e 5')
