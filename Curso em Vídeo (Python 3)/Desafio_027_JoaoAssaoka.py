# DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite Seu Nome Completo: ').split()

print(f'Primeiro Nome: {nome[0]}')
print(f'Último Nome: {nome[-1]}')
