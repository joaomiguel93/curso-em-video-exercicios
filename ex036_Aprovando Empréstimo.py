#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Prazo de pagamento (anos): '))
prestacao = casa / (anos * 12)
if prestacao <= salario * (30 / 100):
    print(f'Empréstimo CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO!')
print(f'Para pagar uma R$ {casa:.2f} em {anos} anos , o valor da prestação será de R$ {prestacao:.2f}')

