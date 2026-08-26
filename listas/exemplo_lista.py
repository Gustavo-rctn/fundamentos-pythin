def mostrar_nome(nomes):
    for nome in nomes:
        print(f"O nome na lista é: {nome}")


lista_nomes = ["Gustavo", "Guilherme o gay", "lara bollos", "Gustavo pimentel",
               "xandipilares"]
mostrar_nome(lista_nomes)


# Adicionar novo nome na lista

def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


adicionar_nome(lista_nomes, "Gustavo")


# Adicionar novo nome em uma posição específica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posção {posicao} da lista: {nomes}")


adicionar_nome_posicao(lista_nomes, "Gustavo", posicao=2)


# Juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nome {novos_nomes} foram inseridos na lista: {nomes}")


novos_nomes = ["Francisco", "Márcio"]
juntar_nomes(lista_nomes, novos_nomes)


# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print('Este nome não existe na lista!')
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido na lista: {nomes}")


remover_nome_pelo_valor(lista_nomes, "Gustavo")


# Removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} é {nomes[posicao]}, foi removido!")


remover_nome_pelo_indice(lista_nomes, 4)


# Descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Nome não encontrado!")
    else:
        posicao = nomes.index(nome)
    posicao = nome.index(nome)
    print(f"A posiçao do nome {nome}, é {posicao}")


encontrar_posicao_pelo_valor(lista_nomes, "Gustavo")


# Contando elementos da lista
def quantidade_de_nome(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")

quantidade_de_nome(lista_nomes)

# Ordenando os elemenetos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

ordenar_nomes(lista_nomes)

# Operações matemáticas
#calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = (total / quantidade)
    print(f"A média é {media}")

notas_semestre = [7.8, 6, 6, 10, 8]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas, reverse=True)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, batata = gerenciar_notas(notas_semestre, 3.5)
print(f"notas ordenada = {notas_ordenadas}")
print(f"A média das notas é {batata}")

#Lista de lista
def adicionar_produto(produtos, produto):
    produto.append(produto)
    print(f"Minha lista de produtos: {produtos[0]}")

lista_produtos = [
    ['Arroz', 2, 32.00],
    ['Feijão', 3, 8.50]
]
novo_produtos = ['Café', 2, 28.00]
adicionar_produto(lista_produtos, novo_produtos)

def quantidade_total_produtos(produtos):
    quantidade = []

    for patati in produtos:
        print(f'rodando laço for em lista_produtos: {produtos[0]}')
        quantidade.append(patati[0])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f'Quantidade de produtos: {quantidade_produtos}')

def valore_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

    return sum(valores)

preco_total_produtos = valore_total_produtos(lista_produtos)
print(f'O valor total dos produtos é {preco_total_produtos}')

# Coloque nome

def cadastrar_e_mostrar_nomes(quantidade=5):
    nomes = []  # Lista vazia para armazenar os nomes

    # Loop para pedir a quantidade desejada de nomes
    for i in range(1, quantidade + 1):
        nome = input(f"Digite o {i}º nome: ")
        nomes.append(nome)  # Adiciona o nome digitado à lista

    # Exibição dos nomes
    print("\nOs nomes cadastrados na lista são:")
    for nome in nomes:
        print(f"- {nome}")

    return nomes


# Executa a função
lista_final = cadastrar_e_mostrar_nomes()
