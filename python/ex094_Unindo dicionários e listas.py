"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
galera = list()
pessoas = dict()

soma = media = 0

while True:
    pessoas.clear()  # limpar dicionário pessoas
    # input nome
    pessoas['nome'] = str(input('Nome: '))
    # input sexo
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas S ou M.')
    # input idade
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())  # adicionando uma cópia do dicionário na lista
    # continuar ou sair
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
        if opcao in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break

print('==' * 20)
# A) Quantas pessoas foram cadastradas
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')

# B) A média de idade
media = soma / len(galera)
print(f'B) A média de idade é {media:5.2f} anos.')

# C) Uma lista com as mulheres
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end='')
print()
# D) Uma lista de pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
