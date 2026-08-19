def contagem_regressiva(numero):
    for i in range(numero, -1, -1):
        print(i)

num = int(input("Digite o número inicial da contagem: "))
contagem_regressiva(num)