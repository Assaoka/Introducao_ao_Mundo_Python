# DESAFIO 004 -  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

Algo = input('Digite Algo: ')

print(f'\nTipo: {type(Algo)}')
print(f'Só tem espaços: {Algo.isspace()}')
print(f'É um número: {Algo.isnumeric()}')
print(f'É alfabético: {Algo.isalpha()}')
print(f'É alfanumérico: {Algo.isalnum()}')
print(f'Está em maiusculas: {Algo.isupper()}')
print(f'Está em minusculas: {Algo.islower()}')
print(f'Está captalizado: {Algo.istitle()}')
