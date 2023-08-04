# DESAFIO 022 - Crie um programa que leia o nome completo de uma pessoa e mostre: 

Nome_Completo = input('Digite Seu Nome Completo: ').strip()

# O nome com todas as letras maiúsculas e minúsculas.
print(f'Nome com MAIÚSCULAS: {Nome_Completo.upper()}')
print(f'Nome com minúsculas: {Nome_Completo.lower()}')

# Quantas letras ao todo (sem considerar espaços).
print(f'Seu nome completo tem {len(Nome_Completo) - Nome_Completo.count(" ")} letras (sem considerar espaços)')

# Quantas letras tem o primeiro nome.
print(f'Seu primeiro nome tem {Nome_Completo.find(" ")} letras')
