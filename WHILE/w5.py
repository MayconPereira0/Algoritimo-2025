
n = int(input("Digite a quantidade de pessoas para ver sua idade: "))

media = []

for i in range(n):
    idade = int(input("Digite sua idade: "))
    media.append(idade)

calcula = sum(media) / n

if calcula >= 0 and calcula <= 25:
    print("media de idades entre 0 e 25")
elif calcula >= 25 and calcula <= 60:
    print("media de idades entre 25 e 60")
elif calcula > 60:
    print("media de idades maior que 60")