# DESAFIO 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('\nQual é o Salário do Funcionário? R$ '))
salário_corrigido = (1.15 if salário <= 1250 else 1.1) * salário

print(f'Quem ganhava R$ {salário:.2f} passa a receber R$ {salário_corrigido:.2f}.\n')
