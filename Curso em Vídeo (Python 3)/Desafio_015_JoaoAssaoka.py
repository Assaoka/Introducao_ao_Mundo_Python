# DESAFIO 015 -Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Q_km = float(input('Qual a quantidade de km percorridos: '))
Q_Dias = int(input('Por quanto dias o carro foi alugado: '))

# R$ 60 por dia + R$ 0,15 por Km rodado
Preço = Q_Dias * 60 + Q_km * 0.15

print(f'O preço é R$ {Preço:.2f}')
