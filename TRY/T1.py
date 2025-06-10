
try:
    n1=int(input("Digite uma palavra: "))
except ValueError:
    print("Digite apenas número")
except:
    print("Erro desconhecido")
finally:
    print("Fim do algoritimo")

