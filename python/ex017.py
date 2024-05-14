# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Compriimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hiponetusa vai medir {:.2f}.'.format(hi))


'''hi = (co ** 2 + ca **2) **(1/2)
print('A hiponetusa vai medir {}.'.format(hi))'''
