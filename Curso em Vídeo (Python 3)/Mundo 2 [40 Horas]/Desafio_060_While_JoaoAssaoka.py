# DESAFIO 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Usando While

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
FIM = '\033[m' # Fim da formatação.

n = int(input(f'\n{NEGRITO}Digite um Número Inteiro Positivo:{FIM} '))
while n < 0:
    n = int(input(f'{NEGRITO}Digite um Número Inteiro {VERMELHO}Positivo:{FIM} '))

print(f'{NEGRITO}{n}! = ', end='')
fatorial = 1
while n > 1:
    print(f'{n}', end=' * ')
    fatorial *= n
    n -= 1
print(f'1 = {fatorial}{FIM}\n')
