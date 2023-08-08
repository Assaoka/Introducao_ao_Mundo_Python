# DESAFIO 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m'


a = float(input('\nDigite o tamanho do primeiro lado: '))
b = float(input('Digite o tamanho do segundo lado: '))
c = float(input('Digite o tamanho do terceiro lado: '))

print(f'{VERMELHO + "Não " if ((a + b < c) or (a + c < b) or (b + c < a)) else VERDE}Formam um Triangulo.{FIM}\n')
