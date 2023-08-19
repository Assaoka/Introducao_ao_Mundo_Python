# DESAFIO 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Formatações de texto para o terminal:
VERMELHO = '\033[1;31m' # 1 = Negrito, 31 = Letra Vermelha
VERDE = '\033[1;32m' # 1 = Negrito, 32 = Letra Verde
FIM = '\033[m' # Fim da formatação.

frase = input('\nDigite uma Frase: ').replace(' ', '').upper()
tam = len(frase)
palíndromo = True

for i in range(0, tam):
    if frase[i] != frase[- i - 1]:
        palíndromo = False
        break

print(f'{VERDE if palíndromo else VERMELHO+"Não "}É Palíndromo.{FIM}\n')
# Outra opção era criar uma variável auxiliar recebendo frase[::-1] e comparar depois diretamente.
