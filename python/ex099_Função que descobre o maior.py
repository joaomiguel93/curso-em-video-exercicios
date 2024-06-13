"""Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep


# Função da barra

def barra():
    print('=' * 40)


# Função Maior

def maior(*args):
    barra()
    # Imprimindo os valores informados
    maior = 0
    print('Analisando os valores informados...')
    sleep(1.5)

    # Analisando os valores
    for valor in args:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if valor > maior:
            maior = valor
    sleep(1)
    print(f'Foram informados {len(args)} valores')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
