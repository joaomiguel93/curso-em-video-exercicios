# Aprimore o desafio anterior, mostrando no final:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0, 3):  # Laço para as linhas
    for c in range(0, 3):  # Laço para as colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-' * 25)
# A) A soma de todos os valores pares digitados.
print(f'Soma dos valores pares: {spar}')

# B) A soma dos valores da terceira coluna.
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3º coluna: {scol}')

# C) O maior valor da segunda linha.
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da  2ª linha: {maior}')
