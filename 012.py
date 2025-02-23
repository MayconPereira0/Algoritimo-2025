#  Faça um algoritmo para uma nutricionaista
#  que receba o peso de uma pessoa, calcule e
#  mostre:
#  a) o novo peso se a pessoa necessitar engordar
#  15% sobre o peso digitado;
#  b) o novo peso se a pessoa necessitar emagrecer
#  20% sobre o peso digitado.

peso = float(input("Informe o peso(Kg): "))

if peso < 60:
    engorda = peso * 0.15
    print(f"precisa engordar: {engorda}Kg")
elif peso >= 80:
    emagrece = peso * 0.20
    print(f"precisa emagrecer: {emagrece}Kg")

