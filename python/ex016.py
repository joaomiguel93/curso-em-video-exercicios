# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#import math
#num = float(input('Digite um número: '))
#print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))


# outra maneira de resolver
from math import trunc
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
