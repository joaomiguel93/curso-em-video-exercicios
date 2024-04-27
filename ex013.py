# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('QUal é o salário do funcionário? R$ '))
reajustado = salario + (salario * (15/100))
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salario, reajustado))
# TESTES

sal1 = float(input('Qual é o salário atual do colaborador? R$ '))
perc = float(input("Qual é o percentual de reajuste: "))
sal2 = sal1 + (sal1 * (perc/100))
print('O reajuste será de R$ {:.2f} e o novo salário do colaborador será R$ {:.2f}.'.format(sal1 * (perc / 100), sal2))
