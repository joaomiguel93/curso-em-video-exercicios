#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
alt = float(input('Altura da parede (m): '))
lar = float(input('Largura da parede (m): '))
area = alt * lar
print('A sua parede tem {}x{} e sua área é de {:.2f} m², você irá precisar de {:.2f}l de tinta.'.format(alt, lar, area, area/2))
