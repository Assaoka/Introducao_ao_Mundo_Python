# DESAFIO 045 - Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
Jogada_Comp = randint(0,2)

# Formatações de texto para o terminal:
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
NEGRITO = '\033[1m'
FIM = '\033[m'

Jokenpô = ['Pedra', 'Papel', 'Tesoura']
Jogada_Jogador = int(input(f'''\nOpções
    {NEGRITO}[0]{FIM} Pedra
    {NEGRITO}[1]{FIM} Papel
    {NEGRITO}[2]{FIM} Tesoura
Escolha sua Jogada: '''))

print(f'\n{NEGRITO}JO')
sleep(1)
print('KEN')
sleep(1)
print(f'PÔ!{FIM}')

if 0 <= Jogada_Jogador <= 2:
    print(f'\nSua Jogada Foi {NEGRITO}{Jokenpô[Jogada_Jogador]}{FIM}')
    print(f'O Computador Escolheu {NEGRITO}{Jokenpô[Jogada_Comp]}{FIM}\n')

    if Jogada_Comp == Jogada_Jogador:
        print(f'Empate, ambos jogaram {Jokenpô[Jogada_Comp]}.\n')
    elif(Jokenpô[Jogada_Comp] == 'Pedra' and Jokenpô[Jogada_Jogador] == 'Papel') or \
        (Jokenpô[Jogada_Comp] == 'Papel' and Jokenpô[Jogada_Jogador] == 'Tesoura') or \
        (Jokenpô[Jogada_Comp] == 'Tesoura' and Jokenpô[Jogada_Jogador] == 'Pedra'):
        print(f'{VERDE}Você venceu!!! Parabéns!!!{FIM}\n')
    else:
        print(f'{VERMELHO}Mais sorte na próxima vez! O Computador Ganhou.{FIM}\n')
else:
    print('Jogada Inválida.\n')
