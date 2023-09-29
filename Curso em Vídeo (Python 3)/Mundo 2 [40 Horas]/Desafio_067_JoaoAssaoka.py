# DESAFIO 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print(f'\n{"+"*50}')
while True:
    num = int(input('Quer Ver a Tabuada de Qual Valor? '))
    if num < 0:
        break
    for i in range (1, 11, 1):
        print(f'{num} * {i:2} = {num * i}')
    print('+'*50)

print('\nPROGRAMA TABUADA ENCERRADO\n')
