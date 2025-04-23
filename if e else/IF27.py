# Verifique se a idade de uma pessoa é menor que 18 ou maior que 65.

idade = int(input('Digite a idade: '))
if idade < 18 or idade > 65:
    print('A idade é menor que 18 ou maior que 65.')
else:
    print('A idade está entre 18 e 65.')