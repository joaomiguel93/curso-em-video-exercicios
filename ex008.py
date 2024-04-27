# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite uma medida em metros): '))
cm = m * 100
mm = m * 1000
print('A medida de {:.2f}m corresponde a {:.0f} cm e {}mm'.format(m, cm, mm))
print('Quilômetro: {:.4f} Km'.format(m / 1000))
print('Hectômetro: {:.2f} Hm'.format(m / 100))
print('Decâmetro: {:.2f} Dam'.format(m / 10))
print('Metro: {:.2f} m'.format(m))
print('Decímetro: {:.2f} dm'.format(m * 10))
print('Centímetro: {:.2f} cm'.format(m * 100))
print('Milímetro: {:.2f} mm'.format(m * 1000))
