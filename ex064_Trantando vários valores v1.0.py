# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0
total = 0
cont = 0
num = int(input('Digite um número [999 para sair]: '))
while num != 999:
    cont += 1
    total += num
    num = int(input('Digite um número [999 para sair]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, total))
