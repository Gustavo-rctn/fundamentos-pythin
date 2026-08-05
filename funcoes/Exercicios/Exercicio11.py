def calcular_salario():
    valor_hora = float(input("Digite o valor por hora trabalhada: "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
    salario = valor_hora * horas_trabalhadas
    print(f"O salário é: R$ {salario:.2f}")

calcular_salario()