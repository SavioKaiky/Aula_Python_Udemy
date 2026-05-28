# condicao = True
# while condicao:
#     nome = input("Qual o seu nome: ")
#     print(f" Seu nome é {nome}")

#contador = 0

# while contador <= 100:
#     contador += 1

#     if contador == 6:
#         continue

#     print(contador)

#     if contador == 40:
#         break

# print("Acabou")

qtd_linha = 5
qtd_coluna = 5
linha = 1

while linha <= qtd_linha:

    coluna = 1

    while coluna <= qtd_coluna:
        
        print(f'{linha=} {coluna=}')
        
        coluna += 1

    linha += 1

print("Acabou")