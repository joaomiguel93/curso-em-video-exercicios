# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year # QUal é o ano do dia que estou usando o programa
nasc = int(input('Ano de nascimento: '))
print('''Escolha uma opção
[ M ] Masculino
[ F ] Feminino''')
sexo = str(input('Qual o seu sexo: ')).upper()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 'M' and idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif sexo == 'M' and idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif sexo == 'M' and idade > 18:
    saldo = idade -18
    print('Você já deviria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif sexo == 'F':
    print('Mulheres não são obrigadas ao serviço militar.')