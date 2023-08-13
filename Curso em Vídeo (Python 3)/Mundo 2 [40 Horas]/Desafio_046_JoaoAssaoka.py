# DESAFIO 046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for i in range(10, -1, -1):
	print(i)
	sleep(1)

Emoji_Fogos = '\U0001F389'
print(Emoji_Fogos * 10)
