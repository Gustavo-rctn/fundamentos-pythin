#Dividir uma string em partes
import urllib


def separar_nome(nome_complemento):
    partes = nome_complemento.split(' ')
    return partes

nome_complemento = input('Digite seu nome completo:')
print(f'Nome em partes: {separar_nome(nome_complemento)}')

#Juntar strings
def criar_nome_completo(partes):
    nome_completo = "_".join(partes)
    return nome_completo

partes_nome = ['Gustavo', 'Henrique', 'Vivaldo', 'Reis']
print(f'Nome em partes: {criar_nome_completo(partes_nome)}')

# Verificar o início e o final de uma string
def analisar_url(url):
    inicia_com_https = url.startswith('https://')
    termina_com_br = url.endswith('.br')
    return inicia_com_https, termina_com_br

url = input('Digite seu url:')

tem_https, tem_br = analisar_url(url)

print(f'Utiliza https: {tem_https}')
print(f'Utiliza br: {tem_br}')

# Verificar se a string contém somente número
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print(f'O valor digitado é uma idade valida')
    else:
        print('Digite somente numeros')

idade = input('Digite sua idade:')
validar_idade(idade)

# Verificar se a string contém somente letras
def validar_nome(nome):
    nome_valida = nome.isalpha()
    if nome_valida:
        print(f'O valor digitado é um nome valido')
    else:
        print('Digite somente letras')

nome = input('Digite sua nome:')
validar_nome(nome)

