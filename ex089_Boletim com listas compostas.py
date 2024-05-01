# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    listaAlunos = [nome, nota1, nota2]  # Lista temporária
    lista.append(listaAlunos)
    opcao = str(input('Quer continuar: [S/N] '))
    if opcao in 'Nn':
        break

print(lista)
print(f'{"NOME":^15} {"MÉDIA":>15}')
for pos, n in enumerate(lista):
    media = (n[1] + n[2]) / 2
    print(f'{pos + 1}. {n[0]:<5}{media:>10}')

while True:
    notasIndiv = int(input('Mostrar notas individuais? [999 interrompe]: '))
    if notasIndiv == 999:
        break
    if notasIndiv
print('<<< PROGRAMA FINALIZADO >>>')
