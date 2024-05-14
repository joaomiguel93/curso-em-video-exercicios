# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em °C: '))
f = (c * (9/5)) + 32
print('A temperatura {:.1f} °C corresponde a {:.1f}°F'.format(c, f))
