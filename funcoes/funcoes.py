def exibir_mensagem():
    print('\nTe amo AMOR!'*10000)

def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2

    print(f'\nO resultado dessa soma é {total}')


def calcular_media():
    valor1 = float(input('\nDigite o primeiro valor: '))
    valor2 = float(input('\nDigite o segundo valor: '))
    media = (valor1 + valor2) / 2
    return media



exibir_mensagem()
somar()
nota_final = calcular_media()
print(f'\nA nota final é {nota_final}')
