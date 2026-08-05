def consumo_combustivel():
    distancia = float(input("Digite a distância percorrida (km): "))
    combustivel = float(input("Digite a quantidade de combustível consumido (L): "))
    consumo_medio = distancia / combustivel
    print(f"O consumo médio é: {consumo_medio:.2f} km/L")

consumo_combustivel()