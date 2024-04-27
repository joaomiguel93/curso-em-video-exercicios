# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Em que cidade você nasceu: '))
print('santo' in cidade)

# Resolução
#cid = str(input('Em que cidade você nasceu? '))
#print(cid[:5] == 'Santo')
cid = str(input('Em que cidade vocÊ nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')