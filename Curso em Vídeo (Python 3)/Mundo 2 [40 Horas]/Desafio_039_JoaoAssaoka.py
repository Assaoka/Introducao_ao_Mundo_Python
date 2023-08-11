# DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

Ano_Nascimento = int(input('\nDigite o ano de nascimento: '))
Ano_Alistamento = Ano_Nascimento + 18
Ano_Atual = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if Ano_Atual == 0: # 0 Corresponde ao Ano Atual
	Ano_Atual = date.today().year

if Ano_Alistamento == Ano_Atual:
	print(f'Como você nasceu no ano de {Ano_Nascimento}, você deve se alistar este ano.\n')
elif Ano_Alistamento < Ano_Atual:
	print(f'Como você nasceu no ano de {Ano_Nascimento}, você deveria ter se alistado em {Ano_Alistamento}.\n Você está {Ano_Atual - Ano_Alistamento} ano(s) atrasado.\n')
else:
	print(f'Como você nasceu no ano de {Ano_Nascimento}, você deverá se alistar daqui a {Ano_Alistamento - Ano_Atual} ano(s).\n Compareça a junta militar em {Ano_Alistamento}.\n')
