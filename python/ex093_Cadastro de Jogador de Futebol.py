# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = {}
dados['nome'] = str(input('Nome do Jogador: '))
totPartidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
dados['gols'] = []

totGols = 0
for p in range(totPartidas):
    dados['gols'].append(int(input(f'  Quantos gols na partida {p+1}: ')))
    totGols += 1
    dados['total'] = sum(dados['gols'])
print()
print('=' * 40)
print(dados)
print('=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 40)
print(f'O jogador {dados['nome']} jogou {len(dados['gols'])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'  - Na partida {i+1}, fez {v}.')
print(f'Foi um total de {sum(dados['gols'])}')
