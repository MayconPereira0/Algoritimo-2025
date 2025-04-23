# Verifique se um número é maior que 0, mas não é múltiplo de 5.

num = int(input('Digite um número: '))
if num > 0 and num % 5 != 0:
    print('O número é maior que 0 e não é múltiplo de 5.')
else:
    print('O número não atende à condição.')