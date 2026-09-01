# Criando a "máquina" (o comando)
def dar_boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

# Usando a "máquina"
dar_boas_vindas("Gustavo")  # Imprime: Olá, Carlos! Seja bem-vindo.

#========================================================================================

def fazer_cafe(tipo_grao, acucar):
    print(f'Você escolheu o café de torra {tipo_grao}, e {acucar} açucar!\n Vamos preparar!')

torra_escolhida = input(' Qual é a torra escolhida?\n [Clara ou Escura] ')
com_ou_sem_acucar = input('Quer seu café com ou sem açucar?')

fazer_cafe(torra_escolhida , com_ou_sem_acucar)

#============================================================================================
def make_cofe(grao, com_acucar, com_creme):
    print(f'A torra escolhida foi {grao}, {com_acucar} açucar e {com_creme} creme \n'
          f'Vamos preparar!')
tipo_torra = input('Que tipo de torra você deseja? [Clara ou Escura]')
acucar = input('Com ou sem açucar?')
creme = input('Quer com ou sem creme junto?')

make_cofe(tipo_torra, acucar, creme )


#===========================================================================================
# Parênteses vazios = a máquina não precisa de nada do lado de fora para começar
def fazer_cafe():
    tipo_grao = input('Qual o tipo de torra? [clara/escura]: ')
    acucar = input('Com açúcar ou sem?: ')
    print(f'Você escolheu o café de torra {tipo_grao} e {acucar}.')

# Chama a função sem passar nada
fazer_cafe()

#=============================================================================================
def somar(a, b):
    soma = a + b
    print(f'A soma de {a} + {b} = a {soma}')


number_a = int(input('Qual a primeira nota? '))
number_b = int(input('Qual a segunda nota? '))

somar(number_a, number_b)

#==============================================================================================
def adicionar_produto(lista):
    mais = input('Tem algum outro produto que deseja adicionar? ')
    lista.append(mais)
    print(f'Produtos no carrinho: {lista}')

# Lista inicial criada fora da função
carrinho = ['café', 'suco']

# Chamada da função passando o carrinho
adicionar_produto(carrinho)








