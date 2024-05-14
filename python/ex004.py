# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
msg = input('Digite algo: ')
print('É um número: ', msg.isnumeric())
print('É um texto? ', msg.isalpha())
print('É alfanumérico? ', msg.isalnum())
print('Só tem espaçoes? ', msg.isspace())
print('Pode ser impresso? ', msg.isprintable())
print('É número decimal? ',msg.isdecimal())
