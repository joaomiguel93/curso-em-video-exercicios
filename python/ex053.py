# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
frase = str(input('Digite uma frase: ')).strip().upper() # strip: tirou os espaços antes e depois e transformou em maísculas (upper)
palavras = frase.split()  # Transformou em uma lista separada pelos os espaços
junto = ''.join(palavras)  # Juntou os itens da lista sem espaços
inverso = ''  # Variável sem valor
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Termo um palídromo!')
else:
    print('A frase digitada não é palíndromo!')
