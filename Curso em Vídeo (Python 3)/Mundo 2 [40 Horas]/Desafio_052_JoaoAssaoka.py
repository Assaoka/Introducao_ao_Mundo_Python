# DESAFIO 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

n = int(input('\nDigite um número inteiro: '))
contador = 0

for i in range (n - 1, 1, -1): # Se ele for divisível por algo entre ele e 1 (excluindo eles), não é primo 
    if n % i == 0:
        contador = 1
        break

if contador == 0 and n != 1:
    print(f'{VERDE}{n} é um número primo.{FIM}\n')
else:
    print(f'{VERMELHO}{n} não é um número primo.{FIM}\n')
    
