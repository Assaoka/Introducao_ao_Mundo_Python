# DESAFIO 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Formatações de texto para o terminal:
NEGRITO = '\033[1m' # 1 = Negrito
FIM = '\033[m' # Fim da formatação.

Soma_Idade = 0
Homem_Mais_Velho = [-1, ""]
Contador_Mulher_Sub20 = 0

for i in range(1, 5):
    print(f'\n{NEGRITO}{i} Pessoa: {FIM}')
    Nome = input('Nome: ')
    Idade = int(input('Idade: '))
    Sexo = input('Sexo (M/F): ').replace(' ', '').upper()

    Soma_Idade += Idade # Vai somando as idades, depois divide por 4
    if Sexo == 'M' and Homem_Mais_Velho[0] < Idade:
        Homem_Mais_Velho = [Idade, Nome]
    elif Sexo == 'F' and Idade < 20:
        Contador_Mulher_Sub20 += 1

print(f'\n{NEGRITO}A média de idade do grupo foi {Soma_Idade/4} anos.')
print(f'O nome do homem mais velho é {Homem_Mais_Velho[1]} e ele tem {Homem_Mais_Velho[0]} anos.')
print(f'Além disso, {Contador_Mulher_Sub20} mulheres têm menos de 20 anos.{FIM}\n')
