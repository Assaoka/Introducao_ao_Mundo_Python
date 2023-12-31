# DESAFIO 059 - Crie um programa que leia dois valores e mostre um menu (somar, multiplicar, maior, novos números, sair do programa) na tela. Seu programa deverá realizar a operação solicitada em cada caso.
# Usando If-Elif-Else (A pedido da Gabrieli Nunes)

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m' # Fim da formatação.

menu = 4
while menu != 5: # Enquanto o usuário não selecionar "Sair do Programa".
    if menu == 1: # Somar
        print(f'{NEGRITO}{A} + {B} = {A + B}{FIM}')
    elif menu == 2: # Multiplicar
        print(f'{NEGRITO}{A} * {B} = {A * B}{FIM}')
    elif menu == 3: # Maior
        if A == B:
            print(f'{NEGRITO}A e B são Iguais.{FIM}')
        else: 
            print(f'{NEGRITO}O Maior Valor é {A if A > B else B}.{FIM}')
    elif menu == 4: # Novos Números
        A = float(input(f'{NEGRITO}A = {FIM}'))
        B = float(input(f'{NEGRITO}B = {FIM}'))
    else: 
        print(f'{NEGRITO}{menu} é um Índice de Operação Inválida.{FIM}')

    menu = int(input(f'\nMenu de Operações:\n    {NEGRITO}[1]{FIM} Somar\n    {NEGRITO}[2]{FIM} Multiplicar\n    {NEGRITO}[3]{FIM} Maior\n    {NEGRITO}[4]{FIM} Novos Números\n    {NEGRITO}[5]{FIM} Sair do Programa\nOperação Desejada: '))

print(f'{NEGRITO}Fim.{FIM}\n')
