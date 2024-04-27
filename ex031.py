# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {:.2f} Km'.format(distancia))
if distancia <=200:
    preco1 = distancia * 0.5
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preco1))
else:
    preco2 = distancia * 0.45
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preco2))
# Resolução
if distancia <= 200:
    preco3 = distancia * 0.50
else:
    preco3 = distancia * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preco3))
