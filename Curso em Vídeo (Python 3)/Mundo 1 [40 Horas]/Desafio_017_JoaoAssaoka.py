# DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

Cateto_Oposto = float(input('Comprimento do Cateto Oposto: '))
Cateto_Adjacente = float(input('Comprimento do Cateto Adjacente: '))

Hipotenusa = (Cateto_Oposto**2 + Cateto_Adjacente**2)**(1/2)

print(f'O comprimento da Hipotenusa é {Hipotenusa} u.c.')
