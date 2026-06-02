# Exercicio com funções

'''Crie uma função que multiplica todos os arguentos
não nomeados recebidos
Retorneo total para uma variavel e mostre o valor
da variável'''

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    

print(mult(1, 2, 3, 4, 5, 6, 7))

