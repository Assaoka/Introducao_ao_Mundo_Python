# DESAFIO 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print("\nVAMOS JOGAR PAR OU ÍMPAR")
vitórias = 0

while True:
    numJogador = int(input('Diga um Valor: '))
    numPC = randint(0, 10);
    resultado = numPC + numJogador
    
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    while tipo != 'P' and tipo !='I':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    
    print(f'Eu joguei {numPC}')
    if resultado % 2 == 0 and tipo == 'P': vitórias += 1
    elif resultado % 2 == 1 and tipo == 'I': vitórias += 1
    else: break
    print(', VOCÊ VENCEU!\nVamos Jogar Novamente...\n\n')

print('\nGAME OVER!', sep = ' ')
if vitórias == 0: print('Mais sorte da próxima vez!\n')
elif vitórias == 1: print('Você venceu 1 vez.\n')
else: print(f'Você venceu {vitórias} vezes.\n')
