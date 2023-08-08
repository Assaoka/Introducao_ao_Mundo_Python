# DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m'  

A = float(input('\nDigite um número: '))
B = float(input('Digite outro número: '))
C = float(input('Digite mais um número: '))

if A > B and A > C:
    print(f'O {NEGRITO}Maior{FIM} Valor é: {NEGRITO}{A}{FIM}.')
    print(f'O {NEGRITO}Menor{FIM} Valor é: {NEGRITO}{B if B < C else C}{FIM}.\n')
elif B > A and B > C:
    print(f'O {NEGRITO}Maior{FIM} Valor é: {NEGRITO}{B}{FIM}.')
    print(f'O {NEGRITO}Menor{FIM} Valor é: {NEGRITO}{A if A < C else C}{FIM}.\n')
else:
    print(f'O {NEGRITO}Maior{FIM} Valor é: {NEGRITO}{C}{FIM}.')
    print(f'O {NEGRITO}Menor{FIM} Valor é: {NEGRITO}{A if A > B else B}{FIM}.\n')
