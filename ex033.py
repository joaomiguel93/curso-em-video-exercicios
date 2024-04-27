# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro valor: '))
n3 = int(input('Terceiro valor: '))
n2 = int(input('Segundo valor: '))
# Número maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número digitado foi {}'.format(maior))
# Número menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor número digitado foi {}'.format(menor))
