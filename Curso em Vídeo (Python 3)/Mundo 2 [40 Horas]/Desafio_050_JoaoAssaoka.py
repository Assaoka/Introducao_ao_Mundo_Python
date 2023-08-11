# DESAFIO 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for i in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    soma += n if n % 2 == 0 else 0

print(f'A soma dos números pares digitados é {soma}')
