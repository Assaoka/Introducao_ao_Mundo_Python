# Aula 11 (Extra) – Cores no Terminal
# Tipo:
NEGRITO = '\033[1m'
ITALICO = '\033[3m'
SUBLINHADO = '\033[4m'
NEGATIVO = '\033[7m'

# Letras:
BRANCO = '\033[30m'
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CIANO = '\033[36m'
CINZA = '\033[37m'

# Fundos:
F_BRANCO = '\033[40m'
F_VERMELHO = '\033[41m'
F_VERDE = '\033[42m'
F_AMARELO = '\033[43m'
F_AZUL = '\033[44m'
F_MAGENTA = '\033[45m'
F_CIANO = '\033[46m'
F_CINZA = '\033[47m'

# FIM
FIM = '\033[m' # Reseta a formatação.

# Como Juntar? '\033[{Tipo};{Letra};{Fundo}m'
AZUL_NEGRITO_F_AMARELO = '\033[1;34;43m' # 1 = Negrito, 34 = Letra Azul, 43 = Fundo Amarelo
print(AZUL_NEGRITO_F_AMARELO + 'Olá, Mundo!' + FIM)
