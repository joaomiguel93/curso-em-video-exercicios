from ex109_Módulos import Moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {Moedas.moeda(p)} é {Moedas.metade(p, True)}.')
print(f'O dobro de R$ {Moedas.moeda(p)} é {Moedas.dobro(p, True)}.')
print(f'Aumentando 10%, temos {Moedas.aumentar(p, 10, True)}.')
print(f'Reduzindo 13%, temos {Moedas.diminuir(p, 13, True)} ')
