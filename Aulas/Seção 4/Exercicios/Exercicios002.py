'''Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.'''
def par_impar(a):
    impar_par = a % 2

    if impar_par == 0:
        return print(f'O número {a} e PAR')
    else:
        return print(f'O número {a} e IMPAR')

numero = int(input("Digite um número: "))

par_impar(numero)
