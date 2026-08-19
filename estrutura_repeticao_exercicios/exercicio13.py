def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primos(inicio, fim):
    for i in range(inicio, fim + 1):
        if eh_primo(i):
            print(i)

i = int(input("Digite o início do intervalo: "))
f = int(input("Digite o fim do intervalo: "))
mostrar_primos(i, f)