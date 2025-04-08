# Crie uma lista de palavras e remova todas que tenham mais de 6 letras.

l = ['python', 'bom', 'ótimo', 'excelente']

print([i for i in l if len(i) <= 6])