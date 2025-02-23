# - Faça um algoritmo que leia uma temperatura 
# em Fahrenheit e calcula a temperatura 
# correspondente em Celsius. Ao final o programa 
# deve exibir as duas temperaturas.–Usar a 
# fórmula: C = (5 * (F-32) / 9).

temp = int(input("Informe a temperatura em graus Fahrenheit: "))

convert = (5*(temp-32) / 9)

print(f"{convert:.2f}")