# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    #  0         1        2
    ['Maria', 'Helena', 'Luiz'], # 0
    #  0         1        2         3        4
    ['João', 'Miguel', 'Arthur', 'Laura', 'Kaiky'], # 1
    #  0         1          2          3          4
    ['Júlia', 'Luiza', 'Guilherme', 'Aline'] # 2
]

# print(*lista)
# print(*string)
# print(*tupla)

# print(salas)

print(*salas, sep='\n')
