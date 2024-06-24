"""Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
e OBRIGATÓRIO nas eleições."""


# Função voto
def voto(nascimento):
    from datetime import date  # biblioteca importada dentro da função
    atual = date.today().year  # calculo da idade
    idade = atual - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal: Input da data de nascimento
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
