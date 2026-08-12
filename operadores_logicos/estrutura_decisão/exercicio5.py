def classificar_nota():
    nota = float(input("Digite uma nota de 0 a 10: "))
    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bom")
    elif nota >= 5:
        print("Regular")
    else:
        print("Insuficiente")

classificar_nota()