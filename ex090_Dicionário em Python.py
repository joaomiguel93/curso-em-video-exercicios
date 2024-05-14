# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

# Classificando a média
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('=-=' * 10)
print(f'  - Nome é {aluno['nome']}')
print(f'  - Média é igual {aluno['media']}')
print(f'  - Situação é {aluno['situacao']}')
