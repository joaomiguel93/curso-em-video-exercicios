"""Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
e OBRIGATÓRIO nas eleições."""
from datetime import date


# Função para calcular a idade
def calcIdade():
    return date.today().year - nascimento


# Função voto
def voto():
    print(f'Com {calcIdade()} anos: ', end='')
    if calcIdade() > 18 and calcIdade() < 60:
        return 'VOTO OBRIGATÓRIO'
    elif calcIdade() >= 60:
        return 'VOTO OPCIONAL'
    else:
        return 'NÃO VOTA'



nascimento = int(input('Em que ano você nasceu? '))
print(voto())
