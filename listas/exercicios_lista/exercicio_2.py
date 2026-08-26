def inserir_aluno(nomes, nome, posicao):
    nomes.insert(posicao, nome)  # insert(posição, elemento)
    print(f'O nome {nome} foi inserido na posição {posicao} da lista: {nomes}')

lista_nomes = ['Ana', 'Bruno', 'Carla']

# Chamando a função com o nome correto e os argumentos definidos
inserir_aluno(lista_nomes, "Gustavo", posicao=2)