#       012345678910
nome = "Luiz Otávio"
contador = 0
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

while contador <= tamanho_nome:
    nova_string = "*"
    nova_string += nome[contador]
    print(nova_string)
    contador += 1