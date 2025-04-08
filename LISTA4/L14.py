# Crie uma lista de palavras e remova todas que tenham menos de 4 letras.

l = ['python', 'é', 'um', 'curso', 'bom']

print([p for p in l if len(p) >= 4])