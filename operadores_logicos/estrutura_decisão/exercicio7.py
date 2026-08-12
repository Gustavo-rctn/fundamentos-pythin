def classificar_temperatura():
    temp = float(input("Digite a temperatura em °C: "))
    if temp < 15:
        print("Frio")
    elif temp <= 25:
        print("Agradável")
    else:
        print("Quente")

classificar_temperatura()