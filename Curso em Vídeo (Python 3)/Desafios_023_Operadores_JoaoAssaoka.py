# DESAFIO 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Usando Operadores

Num = int(input("Digite um Número Inteiro Entre 0 e 9999: "))

print(f'Unidade: {Num % 10}')
print(f'Dezena: {int((Num % 100)/10)}')
print(f'Centena: {int((Num % 1000)/100)}')
print(f'Milhar: {int((Num % 10000)/1000)}')
