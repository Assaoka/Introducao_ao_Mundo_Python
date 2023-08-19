# DESAFIO 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for i in range(1, 6):
    peso = float(input(f'Qual o Peso (kg) da {i}ª Pessoa: '))
    if i == 1:
        maior = menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso

print(f'O menor foi {menor} kg')
print(f'O maior foi {maior} kg')
