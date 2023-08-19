# DESAFIO 062 - Melhore o DESAFIO 61 ("Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão usando a estrutura while."), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

a = float(input(f'\n{NEGRITO}Primeiro termo da PA:{FIM} '))
r = float(input(f'{NEGRITO}Razão da PA:{FIM} '))

n = 10
i = 1
print(f'\n{NEGRITO}Os 10 primeiros termos dessa progressão:{FIM}')
while n != 0:
	exibir = i + n
	while i < exibir:
		print(f'{VERDE}{a + (i - 1) * r}{VERMELHO}', end=" -> ")
		i += 1
	print(f'{VERDE} ... {FIM}\n')

	n = int(input(f'{NEGRITO}Quantos termos adicionais você quer ver:{FIM} '))
print(f'{NEGRITO}Processo Finalizado Após Exibir {i - 1} termos.{FIM}\n')
