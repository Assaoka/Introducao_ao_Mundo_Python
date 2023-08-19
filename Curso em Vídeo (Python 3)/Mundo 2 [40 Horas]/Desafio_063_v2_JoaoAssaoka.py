# DESAFIO 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

N = int(input(f'\nQuantos termos você quer mostrar: {VERDE}'))
if N == 1:
    print(f'{VERDE}0{FIM}\n')
elif N > 1:
    Fibonacci = [0, 1]
    while len(Fibonacci) < N:
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
    print(*Fibonacci, sep=f'{VERMELHO} -> {VERDE}', end=f'{FIM}\n\n') # "*" separa os elementos da lista, por padrão os elementos viriam separados por espaços, para mudar isso usamos o argumento "sep" 
