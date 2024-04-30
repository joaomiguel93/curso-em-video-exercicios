# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Digite um número: '))
while True:
    if 0 <= num <= 20:
        print(f'O número digitado foi {extenso[num]}.')
        opcao = ' '
        while opcao not in 'SN':
            opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
            num = int(input('Digite um número: '))
            if opcao == 'Nn':
                break
    else:
        print('Tente novamente')
        num = int(input('Digite um número: '))
print('Obrigado')
