# DESAFIO 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m'

Preço = float(input('\nQual o Preço do Produto? R$ '))
Condição = int(input(f'''Escolha uma Entre as Opções a Seguir
    {NEGRITO}[1]{FIM} À vista dinheiro/cheque: 10% de desconto
    {NEGRITO}[2]{FIM} À vista no cartão: 5% de desconto
    {NEGRITO}[3]{FIM} À prazo: até 2x sem juros (20% caso 3x ou mais) 
Condição de Pagamento Escolhida: '''))

if Condição == 1: # À vista dinheiro/cheque: 10% de desconto
    print(f'À vista dinheiro/cheque tem {NEGRITO}10% de desconto.{FIM} Então o produto que custava {NEGRITO}R$ {Preço:.2f} custará {0.9 * Preço:.2f}.{FIM}\n')
elif Condição == 2: # À vista no cartão: 5% de desconto
    print(f'À vista no cartão tem {NEGRITO}5% de desconto.{FIM} Então o produto que custava {NEGRITO}R$ {Preço:.2f} custará {0.95 * Preço:.2f}.{FIM}\n')
elif Condição == 3: # À prazo: até 2x sem juros (20% caso 3x ou mais)
    N_Parcelas = int(input('Qual o número de parcelas: '))

    # Está "fora de ordem" porque é improvável o usuário digitar 1. Analisar isso somente no final otimiza o código.     
    if N_Parcelas == 2: # Em até 2x no cartão: preço formal 
        print(f'Pagar em até 2x no cartão {NEGRITO}não dá nenhum benefício.{FIM} Você pagará {NEGRITO} 2 parcelas de R$ {Preço / 2:.2f}{FIM}\n')
    elif N_Parcelas >= 3: # 3x ou mais no cartão: 20% de juros
        print(f'Para pagar em 3x ou mais no cartão {NEGRITO}cobramos 20% de juros.{FIM} Você pagará {NEGRITO} {N_Parcelas} parcelas de R$ {1.2 * Preço / N_Parcelas:.2f}{FIM}\n')
    elif N_Parcelas == 1: # Se é 1 parcela, é á vista no cartão. Deveria ser a Condição 1.
        print(f'À vista no cartão tem {NEGRITO}5% de desconto.{FIM} Então o produto que custava {NEGRITO}R$ {Preço:.2f} custará {0.95 * Preço:.2f}.{FIM}\n')
    else: 
        print(f'Condição de Pagamento {NEGRITO}INVÁLIDA.{FIM}\n')
else:
    print(f'Condição de Pagamento {NEGRITO}INVÁLIDA.{FIM}\n')
