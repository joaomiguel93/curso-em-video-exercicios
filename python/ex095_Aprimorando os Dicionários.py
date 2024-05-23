"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador."""


dados = {}
while True:
    # input do nome
    dados['nome'] = str(input('Nome do Jogador: '))

    # input da quantidade de partidas
    totPartidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    dados['gols'] = []
    totGols = 0

    # Laço para das partidas e input dos gols
    for p in range(totPartidas):
        dados['gols'].append(int(input(f'  Quantos gols na partida {p+1}: ')))
        totGols += 1
        dados['total'] = sum(dados['gols'])
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite S ou N')
    if opcao == 'N':
        break
