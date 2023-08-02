# DESAFIO 020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

Lista_Nomes = [
    input('Nome do Primeiro Aluno: '),
    input('Nome do Segundo Aluno: '),
    input('Nome do Terceiro Aluno: '),
    input('Nome do Último Aluno: ')
]

shuffle(Lista_Nomes)

print(Lista_Nomes)
