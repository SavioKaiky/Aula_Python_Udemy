# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2, nome1)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)