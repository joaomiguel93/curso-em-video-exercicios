from python.ex115.lib.interface import *


# Verifica se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # 'rt' ler o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Cria o arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # Write um arquivo de texto, se não existir, criar (+)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Aquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.readlines())
