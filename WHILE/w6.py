votos = {1: [], 2: [], 3: []}

quant = int(input("Digite a quantidade de elitores: "))

for i in range (quant):
    escolha = int(input("Escolha o candidato: 1, 2, ou 3: "))
    if escolha == 1:
        votos[1].append(escolha)
    elif escolha == 2:
        votos[2].append(escolha)
    elif escolha == 3:
        votos[3].append(escolha)

# print(f"{cand_1},{cand_2},{cand_3}")

contagem = {candidato: len(v) for candidato, v in votos.items()}

vencedor = max(contagem, key=contagem.get)

print(f"Votos por candidato: {contagem}")
print(f"O vencedor foi o candidato {vencedor} com {contagem[vencedor]} votos.")
