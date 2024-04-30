# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Canetas', 1.50,
         'Cadernos', 5.00,
         'Borracha', 3.40,
         'Lápis', 1.20,
         'Caderno', 15.9,
         'Estojo', 12,
         'Apontador', 2.5)
print('-' * 30)
print(f'{"LISTA DE PREÇOS":^40}')  # Mostrar o texto centralizado (^) dentro de 40 caracteres
print('-' * 30)
# Lista em formato tabular
for pos in range(0, len(lista)):  # Para cada posição no range de 0 até o tamanho da lista...
    if pos % 2 == 0:  # Se a posição (pos) for par
        print(f'{lista[pos]:.<22}', end='')  # Preencher com pontos, alinhada a esquerda e mostrar com 22 caracteres
    else:
        print(f'R$ {lista[pos]:>5.2f}')  # Alinhar a direita, com 2 números após a virgula
print('-' * 30)
