# DESAFIO 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (Considerando a idade no fim do ano)

from datetime import date
ano_atual = date.today().year
maiores = menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Ano de Nascimento da {i}ª Pessoa: '))
    if ano_atual - ano_nascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\nMaiores de Idade: {maiores}')
print(f'Menores de Idade: {menores}\n')
