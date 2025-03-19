# Faça um programa que receba uma temperatura 
# e transforme de Fahrenheit para Celsius. A 
# formula de conversão de Fahrenheit para Celsius 
# é a seguinte: C = (5/9) * (F – 32).

temp = int(input("Informe a temperatura em graus Fahrenheit: "))

convert = (5*(temp-32) / 9)

print(f"{convert:.2f}")