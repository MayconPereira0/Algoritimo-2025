# Verifique se a idade de uma pessoa permite votar (maior de 18 anos).

idade = int(input('Digite a idade: '))
if idade >= 18:
    print('Pode votar.')
else:
    print('Não pode votar.')