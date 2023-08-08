# DESAFIO 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Formatações de texto para o terminal:
F_AMARELO = '\033[1;43m' # 1 = Negrito, 43 = Fundo Amarelo
FIM = '\033[m'

n = int(input('\nDigite um número inteiro: '))
print(f'O número {F_AMARELO}{n}{FIM} é {F_AMARELO}{"par" if (n % 2) == 0 else "ímpar"}{FIM}.\n')
