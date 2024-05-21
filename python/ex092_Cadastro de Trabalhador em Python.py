# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

nome = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Nº da CTPS (0 não tem): '))
if ctps > 0:
    anoContracao = int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$ '))

    dados = {'nome': nome, 'idade': ((datetime.now().year) - anoNascimento), 'ctps': ctps, 'contração': anoContracao, 'salario': salario}
    dados ['aposentadoria'] = ((anoContracao + 35) - anoNascimento)
else:
    dados = {'nome': nome, 'idade': ((datetime.now().year) - anoNascimento)}

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
