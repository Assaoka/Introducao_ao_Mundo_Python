# DESAFIO 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Largura = float(input('Largura da Parede: '))
Altura = float(input('Altura da Parede: '))

# Cada litro de tinta pinta uma área de 2 metros quadrados.
Area = Largura * Altura
Q_Tinta = Area / 2

print(f'Área: {Area} m^2')
print(f'Quantidade de Tinta: {Q_Tinta} L')
