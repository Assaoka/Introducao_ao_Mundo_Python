# DESAFIO 048 - Faça um programa que calcule a soma entre todos os números ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for i in range (3, 500 + 1, 6): 
    # Soma dos números impares múltiplo de 3 podemos representar como a soma dos múltiplos de 6 (múltiplo de 3 sempre par) deslocado 3 casas (Tornando o sempre par em sempre impar).
    soma  += i

print(f'\nA soma entre todos os números ÍMPARES múltiplos de três e que se encontram no intervalo de 1 até 500 é {soma}.\n');
