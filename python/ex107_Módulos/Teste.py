import Moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {Moedas.metade(p):.2f}.')
print(f'O dobro de R$ {p:.2f} é R$ {Moedas.dobro(p):.2f}.')
print(f'Aumentando 10%, temos R$ {Moedas.aumentar(p, 10):.2f}.')
print(f'Diminuindo ')
