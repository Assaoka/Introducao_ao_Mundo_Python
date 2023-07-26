# 2-) Ler dois valores para as variáveis A e B e efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

A = input("A = ")
B = input("B = ")

Temp = A
A = B
B = Temp

print(f"\nA = {A}\nB = {B}")
