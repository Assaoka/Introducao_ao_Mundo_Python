# 8-) Faça um programa que encontre as raízes reais de uma equação do segundo grau na forma: ax2 + bx + c = 0. Considere os casos em que delta é igual a zero, maior que zero e menor que zero.

print("Ax2 + Bx + C = 0")
A = float(input("A = "))

if A == 0:
    print("Como A = 0, essa equação não é do segundo grau")
else:
    B, C = float(input("B = ")), float(input("C = "))
    Delta = B**2 - 4 * A * C

    if Delta > 0:
        print(f"Raiz_1 = {(- B + Delta**(1/2))/(2 * A)}\nRaiz_2 = {(- B - Delta**(1/2))/(2 * A)}")
    elif Delta == 0:
        print(f"Raiz: {-B/(2 * A)}")
    else:
        print("Sem Raizes Reais")
