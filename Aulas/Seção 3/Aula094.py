frese = '         Olha só que     , coisa interessante                                '
lista_frase_cruas = frese.split(',')
lista_frase = []
for i, frase in enumerate(lista_frase_cruas):
    lista_frase.append(lista_frase_cruas[i].strip())

print(lista_frase_cruas)
print(lista_frase)
frases_unidas = ', '.join(lista_frase)
print(frases_unidas)