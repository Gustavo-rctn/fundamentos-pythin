# Laço for simples
import time


def mostrar_numeros():
    for i in range(1, 6):
        print(f"O numero atual é {i}")
        time.sleep(2)


mostrar_numeros()


def mostrar_numero_alternado():
    for i in range(0, 20, 2):
        print(f"O numero atual é {i}")


mostrar_numero_alternado()


def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor
    print(total)


somar_numeros()


def mostrar_numeros_pares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f"numero pares = {numero}")


mostrar_numeros_pares()


def mostrar_item_da_lita():
    sacola_de_frutas = ["Maçâ", "BA"
                                "anana", "pera", "Abacate"]
    for fruta in sacola_de_frutas:
        print(f"Na mnha sacola contém {fruta}")


mostrar_item_da_lita()


def laco_alinhado():
    nomes = ["Renam", "Moises", "Rafael"]
    notas = [8, 9, 10]
    for nome in nomes:
        print(f"Nome do aluno: {nome}")
        for nota in notas:
            print(f"Nota do aluno: {nota}")


laco_alinhado()
