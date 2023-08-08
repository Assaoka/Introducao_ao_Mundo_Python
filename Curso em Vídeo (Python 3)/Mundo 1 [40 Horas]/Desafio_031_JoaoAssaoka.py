# DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m'

distância = float(input(f'\n{NEGRITO}Qual a distância da viagem (km): {FIM}'))

# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
preço = (0.5 if distância <= 200 else 0.45) * distância

print(f'Essa viajem é {NEGRITO}{"longa" if distância > 200 else "curta"}{FIM}, então custa {NEGRITO}R$ {preço:.2f}{FIM}.\n')
