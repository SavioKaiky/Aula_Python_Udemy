# import datetime

# # Criando um objeto date com uma data específica
# data_especifica = datetime.date(2023, 10, 26)
# ano_especifico = data_especifica.year
# print(f"O ano da data específica: {ano_especifico}")

# # Criando um objeto datetime com uma data e hora específicas
# datetime_especifico = datetime.datetime(2024, 7, 15, 10, 30)
# ano_datetime_especifico = datetime_especifico.year
# print(f"O ano do datetime específico: {ano_datetime_especifico}")


# Usando datetime.date.today() para obter a data atual
# data_atual_date = datetime.date.today()
# ano_atual_date = data_atual_date.year
# print(f"O ano atual (com date.today()): {ano_atual_date}")

# # Usando datetime.datetime.now() para obter a data e hora atuais
# data_atual_datetime = datetime.datetime.now()
# ano_atual_datetime = data_atual_datetime.year
# print(f"O ano atual (com datetime.now()): {ano_atual_datetime}")


# altura = 1.80

# print(altura ** 2)
# print(altura * altura)

# nome = str(input('Qual o seu nome: ')).capitalize()
# nome2 = nome.title()
# print(f'{nome} com .captalize\n{nome2} com .title')

# numero_1 = 10
# numero_2 = 20
# resultado = numero_1 * numero_2
# print(resultado)

# erando o código a seguir:

# if 0 and 1:
#     print(True and 1)

# if 1 and 1:
#     print(True and 1 and False)
    
# variavel_a = 1 or 0
# variavel_b = 0 or 1
# print(variavel_a, variavel_a)

# nome = 'Maria Carmo'
 
# if ' ' in nome:
#     print(f'O nome {nome} tem espaços.')
# else:
#     print(f'O nome {nome} NÃO tem espaços.')

# numero = 10
 
# if numero > 1:
#     if numero > 2:
#         if numero > 3:
#             print('Número maior que 3')
#         else:
#             print('Número menor que 3')
#     else:
#         print('Número menor que 2')
# else:
#     print('Número menor que 1')


# start = 0
# end = 10
# while start < end:
#     print(start)
#     start += 1

# linhas = 2
# colunas = 2
 
# linha = 1
# while linha <= linhas:
#     coluna = 1
#     while coluna <= colunas:
#         print(linha, coluna)
#         coluna += 1
#     linha += 1


# print(20*'=-' + '=')

# import secrets
# print(secrets.token_hex(32))

# CPF = '703976031'

# print(len(CPF) == 9 and CPF.isdigit())
# soma = 0
# multiplicador = 10
# for digito in CPF:
#     print(digito)
#     soma += int(digito) * multiplicador
#     print(multiplicador)
#     multiplicador -= 1
#     print(soma)
#     soma2 = (soma * 10)
#     print(soma2)
#     resultado = soma2 % 11
#     print("=-=-=")

# print(3*"=-" + "=")
# print(resultado)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)