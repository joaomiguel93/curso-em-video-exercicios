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
        # print(a.readlines())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
