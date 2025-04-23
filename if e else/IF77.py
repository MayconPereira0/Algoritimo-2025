# 77 - Verifique se um número é múltiplo de 3 ou 5, mas não de 7.

num = int(input())
if (num % 3 == 0 or num % 5 == 0) and num % 7 != 0:
    print('Satisfaz a condição')
else:
    print('Não satisfaz a condição')
