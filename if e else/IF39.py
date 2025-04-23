# Verifique se a diferença entre dois números é maior que 20.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
diff = abs(a - b)
if diff > 20:
    print('A diferença é maior que 20.')
else:
    print('A diferença não é maior que 20.')