# - O Senac Hub Academy, necessita de um 
# software para o cálculo da média dos alunos. 
# Sabendo que os alunos receberão 4 notas, uma 
# por bimestre, e posteriormente deverá ser 
# efetuada a média desses alunos, desenvolva um 
# software que solicite as notas dos 4 bimestres, o 
# nome, a idade, o telefone, a turma efetue o 
# cálculo da média, e imprima todos os dados.


nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
tel = input("Telefone: ")
turma = input("Turma: ")
quant = int(input("Informe a quantidade de notas para calcular media: "))

i = 1
notas = []

while i <= quant:
    nota = float(input(f"Informe a nota {i}: "))
    notas.append(nota)
    i += 1




print(f"{nome}\n{idade}\n{tel}\n{quant}")
print(f"{sum(notas)/quant}")


    