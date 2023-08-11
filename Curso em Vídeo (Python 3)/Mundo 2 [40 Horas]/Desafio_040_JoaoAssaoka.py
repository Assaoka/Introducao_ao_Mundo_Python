# DESAFIO 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Formatações de texto para o terminal:
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde 
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
AMARELO = '\033[1;33m' # 1 = Negrito, 33 = Letra Amarela
FIM = '\033[m' # Fim da formatação

Nota_1 =  float(input('\nQual a nota da primeira prova: '))
Nota_2 = float(input('Qual a nota da segunda prova: '))
Média = (Nota_1 + Nota_2) / 2

if Média < 5.0: # Média abaixo de 5.0: REPROVADO
	print(f'{VERMELHO}Sua media foi {Média}. REPROVADO.{FIM}\n')
elif Média >= 5 and Média <= 6.9: # Média entre 5.0 e 6.9: RECUPERAÇÃO
	# Outro modo de fazer a condição acima: "5 <= Média <= 6.9"
	print(f'{AMARELO}Sua média foi {Média}. Estude para a prova de RECUPERAÇÃO.{FIM}\n')
else: # Média 7.0 ou superior: APROVADO
	print(f'{VERDE}Parabéns!!! Sua média foi de {Média}, você está APROVADO.{FIM}\n')
