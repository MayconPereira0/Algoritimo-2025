# - João recebeu seu salário de R$ 1200,00 e
#  precisa pagar duas contas (C1=R$ 200,00 e
#  C2=R$120,00) que estão atrasadas.
#  Como as contas estão atrasadas, João terá de
#  pagar multa de 1% por dia sobre cada conta.
#  Faça um algoritmo que receba a quantidade de
#  dias de atraso, calcule e mostre, quanto restará
#  do salário do João e o valor das contas
#  atualizadas. (Juros Simples)


sal = 1200

quantida = int(input("Informe a quantidade de contas: "))

soma = []
i = 1

while i <= quantida:
    conta = float(input(f"Informe o preço da conta {i}: "))
    atraso = int(input("Informe a quantos dias está atrasada: "))
    multa = conta * (0.01 * atraso)
    total = conta + multa
    soma.append(total)
    i += 1



print(f"O salário restante será de: {sal-sum(soma)}")
