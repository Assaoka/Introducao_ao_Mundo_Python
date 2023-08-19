# DESAFIO 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

Continuar, i = 'S', 0
while Continuar in 'Ss':
    n = int(input('\nDigite um Número Inteiro: '))
    Continuar = input('Continuar (S/N): ').strip()[0]
    if i == 0:
        Maior = Menor = Soma = n
    else:
        Maior = n if n > Maior else Maior
        Menor = n if n < Menor else Menor
        Soma += n
    i += 1
print(f'\nMédia: {Soma/i}\nMaior: {Maior}\nMenor: {Menor}\n')
