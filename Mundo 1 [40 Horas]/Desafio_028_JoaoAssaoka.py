# DESAFIO 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m'

print(f'\n{VERDE}Vou pensar em um numero entre 0 e 5.{FIM}')
numero_sorteado = randint(0, 5)
chute = int(input('Em qual número eu pensei? '))

if chute == numero_sorteado:
    print(f'{VERDE}Parabéns!{FIM} Eu tinha pensado no número {VERDE}{chute}{FIM}.\n')
else:
    print(f'{VERMELHO}Mais sorte na próxima vez!{FIM} Pensei em {VERDE}{numero_sorteado}{FIM} e não no {VERMELHO}{chute}{FIM}.\n')
