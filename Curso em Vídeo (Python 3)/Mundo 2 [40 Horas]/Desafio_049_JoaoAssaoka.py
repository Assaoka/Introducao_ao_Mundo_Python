# DESAFIO 049 - Refaça o DESAFIO 9 ("Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada"), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('\nDigite um número inteiro: '))

print(f'\nTabuada do {n}:')
for i in range(1, 11):
    print(f'{n} * {i:2} = {n * i}')
