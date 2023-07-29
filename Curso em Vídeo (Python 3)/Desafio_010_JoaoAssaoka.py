# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Carteira = float(input('Quanto você tem na carteira? R$ '))
Dolar = float(input('Qual a cotação do dolar? R$ '))

print(f'\nVocê pode comprar U$ {Carteira/Dolar}!')
