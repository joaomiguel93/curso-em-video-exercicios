# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número qualquer: '))
par = numero % 2 # resto da divisão do 'numero' por 2
if par == 0: # se o resto da divisão for 0
    print('O número {} é um número par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
    