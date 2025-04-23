# Verifique se uma pessoa é adulta (18-64 anos).

idade = int(input('Digite a idade: '))
if 18 <= idade <= 64:
    print('Pessoa adulta.')
else:
    print('Pessoa não adulta.')