# Ex 05. Strings
# Faça um programa que leia um nome e imprima apenas a 
# letra do primeiro nome em maiúsculo

nome = input("Digite o nome: ")

nome_form = nome[0].upper() + nome[1:]

print(nome_form)