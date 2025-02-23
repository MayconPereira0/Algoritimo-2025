# Desenvolva um programa 1.0 para auxiliar um 
# azulejista, no qual será solicitado o valor da 
# largura e do comprimento de uma área, e deverá 
# ser informado quanto deverá ser comprado de 
# piso. Fórmula para cálculo de área = largura x 
# comprimento.

l = float(input("Informe a largura da área: "))
c = float(input("Informe o comprimento da área: "))

quant = l * c

print(f"Deverá ser comprado {quant} M² de piso")