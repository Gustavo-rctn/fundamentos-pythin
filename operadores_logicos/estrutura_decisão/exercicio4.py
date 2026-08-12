def verificar_aprovacao():
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

verificar_aprovacao()