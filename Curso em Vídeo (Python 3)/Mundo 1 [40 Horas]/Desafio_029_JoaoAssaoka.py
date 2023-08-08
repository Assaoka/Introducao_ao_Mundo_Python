# DESAFIO 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m'

velocidade = float(input(f'\n{NEGRITO}Qual a Velocidade do Carro (km/h): {FIM}'))

if velocidade > 80:
    multa = (velocidade - 80) * 7 # A multa vai custar R$7,00 por cada Km acima do limite.
    print(f'Você foi multado em {VERMELHO}R$ {multa:.2f}{FIM} por estar a {VERMELHO}{velocidade} km/h.\n')
else:
    print(f'Você estava dentro do limite de velocidade. {VERDE}Parabéns!{FIM}\n')
