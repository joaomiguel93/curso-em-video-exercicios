# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número: '))
print('Escolha uma das bases para conversão:')
print('''[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
base = int(input('Sua opção: '))
if base == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(base)}')
if base == 2:
    print(f'O número {num} convertido para OCTAL é {oct(base)}')
if base == 3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(base)}')
print('>> FIM DO PROGRAMA <<')
