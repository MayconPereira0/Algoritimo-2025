# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperatura, bem como o mês e o ano que ocorreu essa temperatura, 
# e informe ao final a menor e a maior temperaturas informadas, o mês e o ano em que elas ocorrera, bem como a média de todas as temperaturas.

temperaturas = []

print("Digite os dados de temperatura. Para encerrar, digite 'sair' no mês.\n")

while True:
    mes = input("Digite o mês (ou 'sair' para terminar): ").strip()
    if mes.lower() == "sair":
        break

    try:
        ano = int(input("Digite o ano: "))
        temp = float(input("Digite a temperatura (°C): "))
        temperaturas.append((temp, mes, ano))
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")

if len(temperaturas) == 0:
    print("\nNenhuma temperatura foi registrada.")
else:
    maior = temperaturas[0]
    menor = temperaturas[0]
    soma = 0

    for temp, mes, ano in temperaturas:
        soma += temp
        if temp > maior[0]:
            maior = (temp, mes, ano)
        if temp < menor[0]:
            menor = (temp, mes, ano)

    media = soma / len(temperaturas)

    print("\n🔍 Resultados:")
    print(f" Maior temperatura: {maior[0]}°C em {maior[1]} de {maior[2]}")
    print(f" Menor temperatura: {menor[0]}°C em {menor[1]} de {menor[2]}")
    print(f" Média das temperaturas: {media:.2f}°C")
