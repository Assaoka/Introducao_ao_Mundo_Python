# DESAFIO 038 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# Formatações de texto para o terminal:
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
FIM = '\033[m'

n1 = int(input(f'\n{VERDE}Digite um número: {FIM}'))
n2 = int(input(f'{VERMELHO}Digite outro número: {FIM}'))

if n1 > n2:
	print(f'{VERDE}O primeiro valor é maior.{FIM}\n')
elif n2 > n1:
	print(f'{VERMELHO}O segundo valor é maior.{FIM}\n')
else:
	print('Não existe valor maior, os dois são iguais\n')
