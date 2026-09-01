# Converter texto para maiúsculas e minúsculas
from pip._internal.models import index


def formatar_nome(nome):
    #maiusculo = upper()
    nome_maiusculo = nome.upper()
    #minusculo = lower()
    nome_minusculo = nome.lower()

    # nome com primeira letra maiúscula
    nome_camel_case = nome.capitalize()

    return nome_maiusculo, nome_minusculo, nome_camel_case


nome = input('Digite o seu nome:')

#print(formatar_nome(nome)[1])


nome_maiusculo, nome_minusculo, nome_camel_case = formatar_nome(nome)

print(f'Seu nome em maiúsculas: {nome_maiusculo}\n'
      f'Seu nome em minusculas: {nome_minusculo}\n'
      f'Seu nome em camel_case: {nome_camel_case}')

#Remover espaços desnescessarios.
def limpar_texto(texto):
    #.strip remove os espaços do inicio e do final
    texto_limpo = texto.strip()
    #o .lstrip() remove espaços da esquerda
    #o .rstrip() remove espaços da direita
    return texto_limpo

texto_1 = input('Digite uma frase: ')
print(f'texto antes: {texto_1}\n'
      f'texto final: {limpar_texto(texto_1)}\n')


#substituir palavras
def trocar_cidade(cidade):
    # Troca uma palavra por outra
    texto_trocado = cidade.replace(cidade, "Piracicaba")
    return texto_trocado

cidade = input('Digite sua cidade: ')
print(f'Eu moro em {cidade} e me mudei para {trocar_cidade(cidade)}')


#contar caracteres ou ocorrencias
def analisar_texto(texto, letra):
    # contar a quantiade de caracteres
    qtde_caracteres = len(texto)

    #contar a quantidade de ocorrencias
    qtde_letra_a = texto.strip().lower().count(letra)

    return qtde_caracteres,qtde_letra_a

texto_2 = input('Digite uma frase: ')
letra = input('Digite uma letra: ')

qtde_caracteres, qtde_letra = analisar_texto(texto_2, letra)

print(f'Total de caracteres: {qtde_caracteres}\n'
      f'Total de letras {qtde_letra}: {qtde_letra}\n')

# Verificar se uma palavra está presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # Retorna um booleano (True ou False)
    return palavra_presente

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')

print(f'A palavra está presente na frase? {verificar_palavra(frase, palavra)}')

# Encontrar a posição de uma palavra
def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase_2 = input('Digite uma frase: ')
palavra_2 = input('Digite uma palavra: ')

print(f'A posição da palavra é {encontrar_posicao_palavra(frase_2, palavra_2)}')



