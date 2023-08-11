# DESAFIO 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import date
Ano_Atual = date.today().year

Ano_Nascimento = int(input('\nQual o ano de nascimento do atleta: '))
Idade = Ano_Atual - Ano_Nascimento
print(f'O atleta tem {Idade} anos.')

if Idade <= 9: # Até 9 anos: MIRIM
	print('Categoria: MIRIM\n')
elif Idade <= 14: # Até 14 anos: INFANTIL
	print('Categoria: INFANTIL\n')
elif Idade <= 19: # Até 19 anos: JÚNIOR
	print('Categoria: JÚNIOR\n')
elif Idade <= 25: # Até 25 anos: SÊNIOR
	print('Categoria: SÊNIOR\n')
else: # Acima de 25 anos: MASTER
	print('Categoria: MASTER\n')
