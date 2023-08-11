# DESAFIO 042 - Refaça o DESAFIO 35 ("Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."), acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m'

# Leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input('\nDigite o tamanho da primeiro reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if ((a + b < c) or (a + c < b) or (b + c < a)):
	print(f'{VERMELHO}{a}, {b} e {c} Não Formam um Triangulo.{FIM}\n')
else:
	print(f'{VERDE}{a}, {b} e {c} Formam um Triangulo', end=' ')

	# Acrescente o tipo de triângulo será formado
	if a == b == c: # EQUILÁTERO: todos os lados iguais (Condição Equivalente: "a == b and b == c")
		print(f'EQUILÁTERO.{FIM}\n')
    elif a != b != c != a: # ESCALENO: todos os lados diferentes (Possibilidade Equivalente: "a != b and a != c and b != c")
		print(f'ESCALENO.{FIM}\n')
	else: # ISÓSCELES: dois lados iguais, um diferente
		print(f'ISÓSCELES.{FIM}\n')
