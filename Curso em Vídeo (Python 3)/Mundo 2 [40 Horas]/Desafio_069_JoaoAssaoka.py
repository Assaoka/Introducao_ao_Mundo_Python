# DESAFIO 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

maior18 = homens = mulherSub20 = 0
while True:
    print('\n========= Cadastro =========')
    idade = int(input('| Idade: '))
    while True:
        sexo = str(input('| Sexo [M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F': break
    
    if idade > 18: maior18 += 1 # A) quantas pessoas tem mais de 18 anos.
    if sexo == 'M': homens += 1 # B) quantos homens foram cadastrados. 
    if sexo == 'F' and idade < 20: mulherSub20 += 1 # C) quantas mulheres tem menos de 20 anos.

    print('+--------------------------+')
    while True:
        continuar = str(input('| Continuar [S/N]: ')).strip().upper()
        if continuar == 'S' or continuar == 'N': break
    print('============================')
    if continuar == 'N': break

print(f'''\nForam Cadastrados:
 - {maior18} {"Pessoa" if maior18 == 1 else "Pessoas"} com Mais de 18 Anos.
 - {homens} {"Homem" if homens == 1 else "Homens"}.
 - {mulherSub20} {"Mulher" if mulherSub20 == 1 else "Mulheres"} com Menos de 20 Anos.\n''')
