# 7-) Beecrowd | 1012 | Área

A, B, C = input().split() # Lê a linha de entrada e a divide em três valores (A, B e C)
A, B, C = float(A), float(B), float(C) # Converte os valores para float

print(f"TRIANGULO: {A * C/2:.3f}\nCIRCULO: {3.14159 * C**2:.3f}\nTRAPEZIO: {C * (A + B)/2:.3f}\nQUADRADO: {B**2:.3f}\nRETANGULO: {A * B:.3f}")
