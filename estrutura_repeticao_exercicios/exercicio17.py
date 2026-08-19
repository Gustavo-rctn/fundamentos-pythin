def jogo_adivinhacao(numero_secreto):
    palpite = None
    while palpite != numero_secreto:
        palpite = int(input("Adivinhe o número secreto: "))
        if palpite < numero_secreto:
            print("O número secreto é maior.")
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")

jogo_adivinhacao(42)