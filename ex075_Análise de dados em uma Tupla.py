# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('-='*20)
print(f'Você digitou os valores {num}')
print('-='*20)
# A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {num.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não apareceu em nenhuma posição.')

# C) Quais foram os números pares
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')




# Umas das possibilidades de resolução
'''num = cont = 0
while True:
    num = int(input('Digite um valor: '))
    cont += 1
    if cont == 4:
        break
print(f'{num}')
print('Fim')'''
