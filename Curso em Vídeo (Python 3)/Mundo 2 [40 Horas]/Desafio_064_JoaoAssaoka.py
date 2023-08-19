# DESAFIO 060 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('\nDigite um Número Inteiro (999 para parar): '))
Soma = i = 0

while n != 999:
    Soma, i = Soma + n, i + 1
    n = int(input('Digite um Número Inteiro: '))

if i > 0:
    print(f'A soma desses {i} números inteiros é {Soma}.')
print('FIM\n')
