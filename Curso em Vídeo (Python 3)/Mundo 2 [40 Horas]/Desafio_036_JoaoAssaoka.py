# DESAFIO 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Formatações de texto para o terminal:
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
FIM = '\033[m'

# Pergunte o valor da casa
Preço = float(input('\nQual o Valor da Casa: R$ '))
# O salário do comprador
Salário = float(input('Qual o Salário do Comprador: R$ '))
# Em quantos anos ele vai pagar. 
Tempo = int(input('Em quantos anos ele vai pagar: '))

# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
Prestação = Preço / (Tempo * 12)
if Prestação > (0.3 * Salário):
	print(f'\n{VERMELHO}Empréstimo Negado!{FIM}')
	print(f'Prestação de R$ {Prestação:.2f} excede 30% do Salário (R$ {0.3 * Salário:.2f}).\n')
else:
	print(f'\n{VERDE}Empréstimo Aprovado!{FIM}')
	print(f'Prestação de R$ {Prestação:.2f} é menor que 30% do Salário (R$ {0.3 * Salário:.2f}).\n')
