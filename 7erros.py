print("-- Reservatório de Água --")

alt = float(input("Digite a altura (cm): "))
larg = float(input("Digite a largura (cm): "))
comp = float(input("Digite o comprimento (cm): "))
c_diario = float(input("Digite o valor do consumo médio diário (litros/dia): "))

cap_total = (alt * larg * comp) / 1000 
auton_reser = cap_total / c_diario  


print("\nCapacidade do Reservatório:", cap_total, "litros")
print("Autonomia do Reservatório:", auton_reser, "dias")

if auton_reser < 2:
    print("Consumo Elevado")
elif 2 <= auton_reser <= 7:
    print("Consumo Moderado")
else:
    print("Consumo Baixo")
