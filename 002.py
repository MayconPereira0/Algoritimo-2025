#     Construa um programa que exiba a tabuada 
# de um número do número digitado pelo usuário.


num = int(input("Digite o número para ver sua tabuada: "))

i = 1
res = 0

while i <= 10:
    res = num * i
    print(f"{num}*{i}={res}")
    i += 1