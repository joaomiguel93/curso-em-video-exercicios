"""Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele
marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente."""


# Função ficha
def ficha(jogador="<desconhecido>", gol=0):
    return print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():  # se for número então será uma variável int
    g = int(g)
else:
    g = 0

if n.strip() == '':  # Se n for em branco, a função será chamada...
    ficha(gol=g)  # parâmetro gol será o número de gol
else:
    ficha(n, g)
