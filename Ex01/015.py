# Leia dois valores para as variáveis A e B, e
#  efetuar as trocas dos valores de forma que a
#  variável A passe a possuir o valor da variável B e
#  a variável B passe a possuir o valor da variável A.
#  Apresentar os valores trocados.


A = int(input("Digite um número"))
B = int(input("Digite um número"))

A,B = B,A

print(f"{A}\n{B}")

