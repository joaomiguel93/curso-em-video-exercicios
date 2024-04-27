# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#num = int(input('Digite um número: '))
#n1 = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(n1[3]))
#print('Dezena: {}'.format(n1[2]))
#print('Centena: {}'.format(n1[1]))
#print('Milhar: {}'.format(n1[0]))

# Forma matemática de resolução
num2 = int(input('Digite um número: '))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 //100 % 10
m = num2 // 1000 % 10
print('Analisando o número {}'.format(num2))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

