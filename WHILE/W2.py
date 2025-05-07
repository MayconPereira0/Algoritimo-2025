e1 = []
e2 = []
e3 = []
e4 = []
e5 = []
e6 = []

while True:
    print("1 para votar!")
    print("0 para sair!")

    n1 = int(input("Escolha: "))

    if n1 == 1:
        print("1:M, 2:B, 3:C, 4:A 5=nulo, 6 = branco")
        escolha = input("Digite o número referente a escolha do seu candidato: ")
        if escolha == "1":
            e1.append(escolha)
        elif escolha == "2":
            e2.append(escolha)
        elif escolha == "3":
            e3.append(escolha)
        elif escolha == "4":
            e4.append(escolha)
        elif escolha == "5":
            e5.append(escolha)
        elif escolha == "6":
            e6.append(escolha)
        elif escolha == "":
            e6.append(escolha)
        elif escolha != "1" or "2" or "3" or "4":
            e5.append(escolha)
        print(len(e1))
        print(len(e2))
        print(len(e3))
        print(len(e4))
        print(len(e5))
        print(len(e6))
    elif n1 == 0:
            break

nomes = ["M", "B", "C", "A", "Nulo", "Branco"]
votos = [len(e1), len(e2), len(e3), len(e4), len(e5), len(e6)]
mais_votado = votos.index(max(votos))
print(f"\nCandidato com mais votos: {nomes[mais_votado]} ({votos[mais_votado]} voto(s))")
        






