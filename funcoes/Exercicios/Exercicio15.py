def converter_idade():
    idade_anos = int(input("Digite a sua idade em anos: "))
    meses = idade_anos * 12
    dias = idade_anos * 365
    print(f"Você viveu aproximadamente {meses} meses ou {dias} dias.")

converter_idade()