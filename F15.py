# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


num = int(input("Digite um número: "))

fat = 1

for i in range(1, num+1):
    fat *= i
    print(fat)