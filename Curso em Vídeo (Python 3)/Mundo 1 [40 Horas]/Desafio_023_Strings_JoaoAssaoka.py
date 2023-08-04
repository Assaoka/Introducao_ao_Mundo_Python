# DESAFIO 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Usando Strings

Num = str(input("Digite um Número Inteiro Entre 0 e 9999: "))
Tam = len(Num)

print(f'Unidade: {Num[-1]}')
if Tam > 1:
    print(f'Dezena: {Num[-2]}')
if Tam > 2:
    print(f'Centena: {Num[-3]}')
if Tam > 3:
    print(f'Milhar: {Num[-4]}')
