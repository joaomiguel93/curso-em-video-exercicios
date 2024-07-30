from ex108_Módulos import Moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {Moedas.moeda(p)} é {Moedas.moeda(Moedas.metade(p))}.')
print(f'O dobro de R$ {Moedas.moeda(p)} é {Moedas.moeda(Moedas.dobro(p))}.')
print(f'Aumentando 10%, temos {Moedas.moeda(Moedas.aumentar(p, 10))}.')
print(f'Diminuindo ')
