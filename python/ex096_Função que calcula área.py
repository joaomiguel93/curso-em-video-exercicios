"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""

desafio = 'Função de calcula área'
print(f'{desafio}')
print('-' * len(desafio))
print()


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.2f} x {comp:.2f} é de {a:.2f} m².')


# Programa principal
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
