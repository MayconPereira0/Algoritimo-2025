
nome = input("Digite o nome do paciente: ")
cpf = input("Digite o CPF do paciente: ")
rg = input("Digite o RG do paciente: ")
nasc = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
sexo = input("Digite o sexo do paciente (M/F): ")
peso = float(input("Digite o peso do paciente (kg): "))
tipo_sang = input("Digite o tipo sanguíneo do paciente: ")
renda = float(input("Digite a renda mensal do paciente (R$): "))
endereco = input("Digite o endereço do paciente: ")
tel = input("Digite o telefone do paciente: ")
cidade = input("Digite a cidade do paciente: ")
estado = input("Digite o estado do paciente: ")

print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"RG: {rg}")
print(f"Data de Nascimento: {nasc}")
print(f"Sexo: {sexo}")
print(f"Peso: {peso} kg")
print(f"Tipo Sanguíneo: {tipo_sang}")
print(f"Renda Mensal: R${renda:.2f}")
print(f"Endereço: {endereco}")
print(f"Telefone: {tel}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")
