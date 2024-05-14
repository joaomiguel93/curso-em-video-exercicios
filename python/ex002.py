# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Digite seu nome: ')
print('Olá {}! Seja bem vindo ao Curso em Vídeo'.format(nome))

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
# Testes
p1 = input('Qual é seu nome? ')
p2 = input('Qual a sua idade? ')
print('Olá {},'.format(p1), '{} anos é a sua idade, correto?'.format(p2))
