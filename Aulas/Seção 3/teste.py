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

import secrets
print(secrets.token_hex(32))
