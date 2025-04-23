# Verifique se a diferença entre dois números é menor que 10.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
diff = abs(a - b)
if diff < 10:
    print('A diferença é menor que 10.')
else:
    print('A diferença não é menor que 10.')