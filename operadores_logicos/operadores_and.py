# Operador and

def pode_dirige():
    idade = int(input('Digite a idade: '))
    TEM_HABILITACAO = True

    autorizado = idade >= 18 and TEM_HABILITACAO
    return idade, TEM_HABILITACAO

print(f"Usuário pode dirigir? {autorizado}")

pode_dirige()
