# DESAFIO 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

i = total = num1000 = 0
maisBarato, produto = ['Nome', 0.00], ['Nome', 0.00] # Nome e Preço
while True:
    i += 1
    print(f'\n====== Produto {i:2} ======')
    produto[0] = str(input('| Nome: ')).strip().upper()
    produto[1] = float(input('| Preço: R$ '))

    total += produto[1]
    if produto[1] > 1000: num1000 += 1
    if i == 1 or maisBarato[1] > produto[1]: 
        maisBarato[0] = produto[0]
        maisBarato[1] = produto[1]

    while True:
        continuar = str(input('| Continuar [S/N]: ')).strip().upper()
        if continuar == 'S' or continuar == 'N': break
    if continuar == 'N': break

print(f'''\n------------------------
| A) O Total foi R$ {total:0.2f}
| B) {num1000} {"Produto Custa" if num1000 == 1 else "Produtos Custam"} Mais de R$ 1000.00
| C) O Produto Mais Barato é {maisBarato[0]}, que saiu por R$ {maisBarato[1]:0.2f}\n''')
