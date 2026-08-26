def adicionar_nome(nome, posicao, alunos):
    alunos.append(posicao, nome)
    print(alunos)

lista_nomes = ['gustavo', 'gui', 'lara', 'ferraz', 'pimenta']

nome = input("Digite o nome do aluno: ")
posicao = int(input("Digite a posição: "))

adicionar_nome(nome, posicao, lista_nomes)