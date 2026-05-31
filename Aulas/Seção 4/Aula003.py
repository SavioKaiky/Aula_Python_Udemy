"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma (x, y, z=None):
    if z is not None:
        a = x + y + z
        print(f'{x=} {y=} {z=} {a}')
    else:
        a = x + y
        print(f'{x=} {y=} {a}')


soma(1, 2)
soma(3, 5)
soma(180, 20)
soma(3, 5, 0)