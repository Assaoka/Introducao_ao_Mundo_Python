# DESAFIO 071 -  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cédulas = [50, 20, 10, 1]
print('\n{:=^40}'. format('Banco Assaoka'))

valor = int(input('Quanto Você Quer Sacar: R$ '))
for i in cédulas:
	print(f'| {valor // i} cédula{"s" if valor // i != 1 else ""} de R$ {i},00')
	valor = valor % i
print('{:=^40}\n'. format(''))
