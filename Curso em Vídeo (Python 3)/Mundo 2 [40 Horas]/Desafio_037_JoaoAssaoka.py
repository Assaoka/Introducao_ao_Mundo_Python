# DESAFIO 037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m'

Num = int(input('\nDigite um Número Inteiro: '))

# Menu de opções:
Op = int(input(f'''Opções:
	{NEGRITO}[1]{FIM} Binário
	{NEGRITO}[2]{FIM} Octal
	{NEGRITO}[3]{FIM} Hexadecimal
Você gostaria da conversão para: '''))

if Op == 1:
	print(f'{Num} em binário é {bin(Num)[2:]}\n')
elif Op == 2:
	print(f'{Num} em octal é {oct(Num)[2:]}\n')
elif Op == 3:
	print(f'{Num} em hexadecimal é {hex(Num)[2:]}\n')
else:
	print(f'Opção Inválida!\n')
