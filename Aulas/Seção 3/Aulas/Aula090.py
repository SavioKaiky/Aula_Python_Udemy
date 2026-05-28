lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))
lista_enumerada2 = enumerate(lista)


print(lista_enumerada)
print(' ')
print(lista_enumerada2)
print(' ')

for indice, nome in enumerate(lista):
    print(indice, nome)
print(' ')


for tupla_enumarada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumarada:
        print(f'\t{valor}')


# for item in lista_enumerada:
#     print(item)
