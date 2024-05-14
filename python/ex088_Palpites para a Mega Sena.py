# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos você quer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {quant} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)






# Resolução errada
"""palpites = []  # Lista de palpites da mega
print('-' * 30)
print(f'{'JOGO DA MEGA SENA':^30}')
print('-' * 30)
qtdeJogos = int(input('Quantos jogos você quer? '))  # Input com a quantidade de jogos da Mega
for j in range(0, qtdeJogos):
    jogo = []
    for valores in range(6):
        sorteio = randint(1, 60)
        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)
    jogo.sort()

    print(f'Jogo {j+1}: {jogo} ')"""
