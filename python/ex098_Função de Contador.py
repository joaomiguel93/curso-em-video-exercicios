"""Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:  # Se o passo for igual a 0, considerar igual a 1
        p = 1
    print('=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('>>> FIM DO PROGRAMA <<<')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('>>> FIM DE PROGRAMA <<<')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 30)
print('Agora é sua vez: ')
inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))
passo = int(input('Digite o passo: '))
print('=' * 30)
contador(inicio, fim, passo)
print( )
