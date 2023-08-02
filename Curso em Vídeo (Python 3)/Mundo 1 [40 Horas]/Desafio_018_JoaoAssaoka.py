# DESAFIO 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

Angulo = float(input('Digite um ângulo (Em Graus): '))
Angulo = radians(Angulo) # Convertendo pra Radianos

print(f'\nAngulo em Radianos: {Angulo:.2f}')
print(f'Seno: {sin(Angulo):.2f}')
print(f'Cosseno: {cos(Angulo):.2f}')
print(f'Tangente: {tan(Angulo):.2f}')
