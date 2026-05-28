"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
while True:

    num_str = input('Digite um número inteiro: (ex: 1, 2, 3, ...) ')


    if num_str.isdigit():
        num_int = int(num_str)
        par = num_int % 2

        if par == 0:
            print(f'O número {num_int} e um número par.')
        elif par != 0:
            print(f'O número {num_int} é um número impar.')
    else:
        print(f'O número {num_str} não e um número inteiro.')

    if num_str in ['Sair', 'sair']:
        break