# DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:

frase = str(input('Digite Uma Frase: ').strip().upper())

# Quantas vezes aparece a letra "A"
print(f'A letra "A" apareceu {frase.count("A")} vezes')

# Em que posição ela aparece a primeira vez
print(f'A primeira vez que a letra "A" aparece é {frase.find("A")}')

# Em que posição ela aparece a última vez.
print(f'A última vez que a letra "A" aparece é {frase.rfind("A")}')
