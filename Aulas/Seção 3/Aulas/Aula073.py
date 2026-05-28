# numeros = range(0,100,8)

# for numero in numeros:
#     print(numero)

texto = iter('Luiz') # iterável

iteratador = iter(texto) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
