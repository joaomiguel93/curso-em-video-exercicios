"""Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior."""
# Importando a randint
from random import randint
from time import sleep

# Criando uma lista para os números sorteados
numeros = []


# Função de sorteio
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        valor = randint(1, 10)
        numeros.append(randint(1, 10))  # Adicionando os números sorteados na lista
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
    print('Pronto!')


# Criando a função para somar os números pares
def somaPar(lista):
    par = 0
    for valor in lista:
        if valor % 2 == 0:
            par += valor
    print(f'Somando os valores pares de {lista}, temos {par}')


sorteia()
somaPar(numeros)
