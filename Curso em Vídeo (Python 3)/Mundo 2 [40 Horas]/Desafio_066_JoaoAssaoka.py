# DESAFIO 066 - Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

i = soma = 0
while True:
    n = int(input('Digite um Número Inteiro (999 para parar): '))
    if n == 999:
        break
    soma += n
    i += 1
if i > 0:
    print(f'\nVocê Digitou {i} Números e a Soma Deles é {soma}\n')
else:
    print('\nFim\n')
