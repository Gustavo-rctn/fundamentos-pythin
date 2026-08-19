def menu():
    opcao = 0
    while opcao != 4:
        print("\n--- MENU INTERATIVO ---")
        print("1. Exibir números de 1 a 10")
        print("2. Exibir números pares de 1 a 20")
        print("3. Exibir tabuada de um número")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            for i in range(1, 11):
                print(i, end=" ")
            print()
        elif opcao == 2:
            for i in range(1, 21):
                if i % 2 == 0:
                    print(i, end=" ")
            print()
        elif opcao == 3:
            num = int(input("Digite um número: "))
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
        elif opcao == 4:
            print("Saindo do programa...")
        else:
            print("Opção inválida! Tente novamente.")


menu()