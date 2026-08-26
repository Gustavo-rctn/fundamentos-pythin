def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(f'Os convidados são: {convidados}')

lista_convidados = ['Ana', 'Bruno', 'Carla']
novos_convidados = ['Guilhermina', 'gustavinho pimentinha']
adicionar_convidados(convidados=lista_convidados, novos_convidados=novos_convidados)