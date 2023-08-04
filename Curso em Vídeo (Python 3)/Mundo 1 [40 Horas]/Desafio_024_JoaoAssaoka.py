# DESAFIO 024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Cidade = input('Qual o Nome da Cidade: ').upper().split() # Lista de Palavras que formam o nome em maiúscula

print(f'Nome da Cidade começa com "SANTO": {Cidade[0] == "SANTO"}')
