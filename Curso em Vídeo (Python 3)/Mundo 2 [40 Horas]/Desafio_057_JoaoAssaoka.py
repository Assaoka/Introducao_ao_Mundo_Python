# DESAFIO 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

Sexo = input('\nSexo (M/F): ').strip().upper()[0]
while 'M' != Sexo != 'F':
    Sexo = input(f'{VERMELHO}{Sexo}{FIM} é uma Entrada Inválida. Sexo ({VERMELHO}M/F{FIM}): ').strip().upper()[0]

print(f'\n{VERDE}Sexo Definido como {Sexo}.{FIM}\n')
