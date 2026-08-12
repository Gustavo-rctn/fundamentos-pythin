def sistema_votacao():
    idade = int(input("Digite a sua idade: "))
    if idade < 16:
        print("Não pode votar")
    elif idade in (16, 17) or idade >= 70:
        print("Voto opcional")
    else:
        print("Voto obrigatório")

sistema_votacao()