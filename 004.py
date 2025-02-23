# Desenvolva um programa em sua versão 1.1 
# para auxiliar o azulejista, no qual além de calcular 
# quantidade de piso a ser comprada, deverá 
# também considerar 15% a mais de piso, tendo 
# em vista os recortes de cantos

l = float(input("Informe a largura da área: "))
c = float(input("Informe o comprimento da área: "))

quant = (l * c)

print(f"Deverá ser comprado {quant+(0.15*quant)} M² de piso")