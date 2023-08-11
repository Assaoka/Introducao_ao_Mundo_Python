# DESAFIO 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

Peso = float(input('\nDigite seu peso (Kg): '))
Altura = float(input('Digite sua altura (m): '))
IMC = Peso / (Altura ** 2)

print(f'\nSeu IMC é {IMC:.1f}.')
if 18.5 > IMC: # IMC abaixo de 18,5: Abaixo do Peso
    print('Classificação: Abaixo do Peso')
elif 25 >= IMC: # Entre 18,5 e 25: Peso Ideal
    print('Classificação: Peso Ideal')
elif 30 >= IMC: # 25 até 30: Sobrepeso
    print('Classificação: Sobrepeso')
elif 40 >= IMC: # 30 até 40: Obesidade
    print('Classificação: Obesidade')
else: # Acima de 40: Obesidade Mórbida
    print('Classificação: Obesidade Mórbida')
