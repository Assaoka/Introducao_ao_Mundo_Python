# DESAFIO 059 - Crie um programa que leia dois valores e mostre um menu (somar, multiplicar, maior, novos números, sair do programa) na tela. Seu programa deverá realizar a operação solicitada em cada caso.
# Usando Match Case

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m' # Fim da formatação.

menu = 4
while menu != 5: # Enquanto o usuário não selecionar "Sair do Programa".
    match menu: # A sintaxe de correspondência (match) foi introduzida no Python 3.10. Se você estiver usando uma versão anterior do Python, você precisará substituir o padrão de correspondência por estruturas if-elif-else (resolvido dessa maneira nesse mesmo repositório a pedido da Gabrieli Nunes).
        case 1: # Somar
            print(f'{NEGRITO}{A} + {B} = {A + B}{FIM}')
        case 2: # Multiplicar
            print(f'{NEGRITO}{A} * {B} = {A * B}{FIM}')
        case 3: # Maior
            if A == B:
                print(f'{NEGRITO}A e B são Iguais.{FIM}')
            else: 
                print(f'{NEGRITO}O Maior Valor é {A if A > B else B}.{FIM}')
        case 4: # Novos Números
            A = float(input(f'{NEGRITO}A = {FIM}'))
            B = float(input(f'{NEGRITO}B = {FIM}'))
        case _: # Opção Não Encontrada
            print(f'{NEGRITO}{menu} é um Índice de Operação Inválido.{FIM}')

    menu = int(input(f'\nMenu de Operações:\n    {NEGRITO}[1]{FIM} Somar\n    {NEGRITO}[2]{FIM} Multiplicar\n    {NEGRITO}[3]{FIM} Maior\n    {NEGRITO}[4]{FIM} Novos Números\n    {NEGRITO}[5]{FIM} Sair do Programa\nOperação Desejada: '))

print(f'{NEGRITO}Fim.{FIM}\n')
