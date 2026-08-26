def adicionar_nota(notas, nota):
    notas.append(nota)

def remover_nota(notas, nota):
    notas.remove(nota)

def media_notas(notas):
    return sum(notas) / len(notas)

boletim = [6.0, 7.0]
adicionar_nota(boletim, 9.0)
remover_nota(boletim, 6.0)
print(f"\nEx 15 - Boletim atual: {boletim} | Média: {media_notas(boletim):.2f}")