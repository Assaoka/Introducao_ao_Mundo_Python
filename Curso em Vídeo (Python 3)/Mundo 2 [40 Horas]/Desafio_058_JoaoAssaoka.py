# DESAFIO 058 - Melhore o jogo do DESAFIO 28 ("Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.") onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

print(f'\n{NEGRITO}Vou pensar em um numero entre 0 e 10.')
print('Pensando', end='') # Coloca 3 pontos com intervalo de 1s entre as impressões
for _ in range(3):
    print('.', end='', flush=True)
    sleep(1)
Resposta = randint(0, 10)

print(' Tente acertar o número que pensei!')
Chute = int(input(f'\n{NEGRITO}1ª Tentativa:{FIM} '))
Tentativas = 1

while Chute != Resposta:
    Erro = abs(Resposta - Chute)
    if Erro <= 2: # Está a no máximo 2 de distancia da resposta
        print(f'\n{NEGRITO}Ta Quente!!!')
    elif Erro == 3: # Está a 3 de distancia, nem perto nem longe
        print(f'\n{NEGRITO}Ta Morno!!!')
    else: # Mais de 3 unidades da resposta, bem longe
        print(f'\n{NEGRITO}Ta Frio!!!')
    Tentativas += 1
    Chute = int(input(f'{VERMELHO}{Tentativas}ª Tentativa:{FIM} '))

# A mensagem de vitoria varia de acordo com o número de tentativas
if Tentativas == 1: # Acertou de primeira
    print(f'{VERDE}Uau!!! Você acertou de Primeira.{FIM}\n')
elif Tentativas == 11: # Chutou as 11 possibilidades
    print(f'{VERDE}Sorte no jogo, azar no amor. 11 possibilidades 11 tentativas, logo você casa.{FIM}\n')
elif Tentativas > 5: # Chutou mais da metade das possibilidades
    print(f'{VERDE}Você teve que tentar {Tentativas} vezes. Mais sorte na próxima vez!{FIM}\n')
else: # Chutou menos da metade e não é 1
    print(f'{VERDE}Parabéns, você acertou na {Tentativas}ª vez.{FIM}\n')
