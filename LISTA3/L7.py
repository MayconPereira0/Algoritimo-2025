# Crie uma lista e utilize min() para encontrar o segundo menor valor.

lista = [1,2,3,4,5]

menor = min(lista)

lista.remove(menor)

print(min(lista))