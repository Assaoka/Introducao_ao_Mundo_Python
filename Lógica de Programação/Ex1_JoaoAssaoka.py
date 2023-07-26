# 1-) Faça um programa que lê o valor da cotação do dólar em um determinado dia e em seguida lê uma quantia em dólares. Realize a conversão para reais.

Cot_Dolar = float(input("Qual a cotação do dólar hoje? "))
N_Dolares = float(input("Quantos dólares você tem? $ "))
print(f"Você tem $ {N_Dolares:.2f}, considerando a cotação atual como {Cot_Dolar:.2f}, você tem R$ {Cot_Dolar * N_Dolares:.2f}")
