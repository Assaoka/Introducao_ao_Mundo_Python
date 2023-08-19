# DESAFIO 063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

N = int(input(f'\nQuantos termos você quer mostrar: '))
if N == 1:
    print('0')
if N > 1:
    print('0 -> 1', end='')
    n1, n2 = 0, 1
    N -= 2 # 0 e 1 já foram
    while N > 0:
        print(f' -> {n1 + n2}', end='')
        n1, n2 = n2, n1 + n2
        N -= 1
print('\n')
