lista = ['Maria', 'Helena', 'Luiz', 'Kaiky']
lista.append('João')
lista.append('Jorge')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

for i, lista in enumerate(lista):
    print(f'indice: {i}, Nome: {lista}')
