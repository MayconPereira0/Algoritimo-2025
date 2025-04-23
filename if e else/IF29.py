# Verifique se a pessoa tem mais de 60 anos ou é menor que 18 anos.

idade = int(input('Digite a idade: '))
if idade > 60 or idade < 18:
    print('Pessoa com mais de 60 anos ou menor que 18 anos.')
else:
    print('Pessoa entre 18 e 60 anos.')