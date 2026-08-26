notas_turma = [7.5, 6.0, 8.5, 9.0, 5.5]

def adicionar_nota_sis(notas, nota):
    notas.append(nota)

def inserir_nota_sis(notas, nota, posicao):
    notas.insert(posicao, nota)

def adicionar_varias_sis(notas, novas_notas):
    notas.extend(novas_notas)

def remover_nota_sis(notas, nota):
    notas.remove(nota)

def remover_ultima_sis(notas):
    return notas.pop()

def encontrar_posicao_sis(notas, nota):
    return notas.index(nota)

def quantidade_notas_sis(notas):
    return len(notas)

def ordenar_notas_sis(notas):
    return sorted(notas)

def notas_inversas_sis(notas):
    return list(reversed(notas))

def somar_notas_sis(notas):
    return sum(notas)

def calcular_media_turma_sis(notas):
    return sum(notas) / len(notas)

print("\nEx 19 - Demonstração do Sistema Completo:")
adicionar_nota_sis(notas_turma, 10.0)
inserir_nota_sis(notas_turma, 8.0, 2)
adicionar_varias_sis(notas_turma, [6.5, 7.0])
remover_nota_sis(notas_turma, 5.5)
remover_ultima_sis(notas_turma)

print(f"Notas Atuais: {notas_turma}")
print(f"Posição da nota 9.0: {encontrar_posicao_sis(notas_turma, 9.0)}")
print(f"Quantidade de notas: {quantidade_notas_sis(notas_turma)}")
print(f"Notas Ordenadas: {ordenar_notas_sis(notas_turma)}")
print(f"Notas Invertidas: {notas_inversas_sis(notas_turma)}")
print(f"Soma das Notas: {somar_notas_sis(notas_turma)}")
print(f"Média Geral da Turma: {calcular_media_turma_sis(notas_turma):.2f}")