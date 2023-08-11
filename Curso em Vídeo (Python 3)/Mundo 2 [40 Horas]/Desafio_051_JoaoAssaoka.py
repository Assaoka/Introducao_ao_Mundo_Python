# DESAFIO 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

a = float(input('\nPrimeiro termo da PA: '))
r = float(input('Razão da PA: '))

print('\nOs 10 primeiros termos dessa progressão:')
for i in range (1, 11):
    print(f'{VERDE}{a + (i - 1) * r}{VERMELHO}', end=" -> ")
print(f'{VERDE}Fim.{FIM}\n')
