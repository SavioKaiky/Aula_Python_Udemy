#       012345678910
#nome = "Luiz Otávio"
nome = "Savio Kaiky Lopes de Carvalho"
indice = 0
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

# while indice <= tamanho_nome:
#     nova_string = "*"
#     nova_string += nome[indice]
#     print(nova_string)
#     indice += 1
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1

novo_nome += "*"
print(novo_nome)