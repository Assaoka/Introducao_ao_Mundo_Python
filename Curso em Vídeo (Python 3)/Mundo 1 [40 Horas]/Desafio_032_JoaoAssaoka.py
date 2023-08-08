# DESAFIO 032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m'

ano = int(input('\nDigite um Ano para Analisar (Digite 0 para o Ano Atual): '))
ano = date.today().year if ano == 0 else ano # 0 Corresponde ao Ano Atual

# É bissexto? (É bissexto se for divisível por 4, mas não for divisível por 100, a não ser que seja divisível por 400)
resposta =  ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

print(f'{ano}{VERMELHO + " não" if resposta == False else VERDE} é um ano bissexto.{FIM}\n')
