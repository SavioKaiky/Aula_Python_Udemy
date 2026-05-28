'''
Lista de lista e seus índices
'''

salas = [
    #  0         1        2
    ['Maria', 'Helena', 'Luiz'], # 0
    #  0         1        2         3        4
    ['João', 'Miguel', 'Arthur', 'Laura', 'Kaiky'], # 1
    #  0         1          2          3          4
    ['Júlia', 'Luiza', 'Guilherme', 'Aline'] # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][4][2])

for sala in salas:
    print(f'Sala: {sala}')
    for aluno in sala:
        print(aluno)