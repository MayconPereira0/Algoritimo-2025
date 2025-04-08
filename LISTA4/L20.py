# Crie uma lista e remova os espaços em branco dos elementos.

l = ['  python', 'listas ', '  programar  ']
ls = [p.strip() for p in l]
print(ls)