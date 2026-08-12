def verificar_velocidade():
    velocidade = float(input("Digite a velocidade do veículo (km/h): "))
    if velocidade <= 60:
        print("Velocidade permitida")
    elif velocidade <= 80:
        print("Atenção: velocidade acima do permitido")
    else:
        print("Multa por excesso de velocidade")

verificar_velocidade()