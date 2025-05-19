
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

lista = []

for i in range(n1+1, n2+1):
    lista.append(i)

print(sum(lista))
