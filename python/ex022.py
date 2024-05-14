# print("""Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.
nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Maiúsculas:',nome.upper())
print('Minúscula:', nome.lower())

# Quantas letras ao todo (sem considerar espaços)
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))

# Quantas letras tem o primeiro nome
lista = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(lista[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))