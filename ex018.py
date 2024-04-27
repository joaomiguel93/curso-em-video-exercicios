# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {:.2f} tem o COSSENO DE {:.2f}'.format(ang, cos))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ang, tan))
