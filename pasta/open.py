with open("pasta/text.txt", "r") as f:
    for i in f:
        if "João" in i.lower():
            print(i)




while True:
            try:
                nome = str(input('Nome completo: '))
                if nome.isalpha(): # como fazer os espaços valarem também??
                    break
                else:
                    print('Digite apenas letras.')
            except ValueError:
                print('Digite apenas letras!') 