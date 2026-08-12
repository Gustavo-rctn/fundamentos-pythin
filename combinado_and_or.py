#Operadores and e or

def posso_entrar_no_show_do_veih():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade?"))
    nome_esta_na_lista = bool(input("Seu nome está na lista?"))

    posso_entrar = (nome_esta_na_lista or POSSUI_INGRESSO)and dade >= 18

    print(f"Vou conseguir entrar no show? {posso_entrar}")

posso_entrar_no_show_do_veih()