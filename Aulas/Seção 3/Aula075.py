# texto = iter("Luiz")
# print(texto)

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = "Kaiky"

iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)    
    except StopIteration:
        break