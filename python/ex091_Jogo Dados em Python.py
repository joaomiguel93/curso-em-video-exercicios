# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
raking = []
print('  == Valores Sorteados ==  ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
raking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==  ')
print('Montando ...')
sleep(2)
for i, v in enumerate(raking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)


