def login():
    e_mail = ("guhvreis@gmail.com")
    senha = "1234"
    codigo_secreto = "#456@"

    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")
    codigo_secreto_input = input("Digite seu codigo secreto: ")

    if e_mail_input == e_mail and senha_input == senha:
        print("Logado com sucesso!")
        acessar_admin = input("Acessar o administrador: (Digite S ou N)")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("Acesso Adm Liberado")
            else:
                print("Erro acesso Adm Negado")
        elif acessar_admin == "N":
                print("Voce acessou como um usuario")
    else:
        print("E-mail ou senha incorretos!")

login()