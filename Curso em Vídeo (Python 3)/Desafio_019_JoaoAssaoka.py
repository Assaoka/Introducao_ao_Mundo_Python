# DESAFIO 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

Lista_Nomes = [
    input('Nome do Primeiro Aluno: '),
    input('Nome do Segundo Aluno: '),
    input('Nome do Terceiro Aluno: '),
    input('Nome do Último Aluno: ')
]

print(f'O aluno escolhido para apagar o quadro é: {choice(Lista_Nomes)}')
