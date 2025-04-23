# Verifique se um número é múltiplo de 2 e 3.

num = int(input('Digite um número: '))
if num % 2 == 0 and num % 3 == 0:
    print('O número é múltiplo de 2 e 3.')
else:
    print('O número não é múltiplo de 2 e 3.')