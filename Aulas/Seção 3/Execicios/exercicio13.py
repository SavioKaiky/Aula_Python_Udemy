"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
     0 1 2 3 4 5 6 7 8 9 10
CPF: 7 4 6 8 2 4 8 9 0 7 0

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re

# inicio do algoritimo
while True:
    print('Gerador de CPF')
    print(22 * '=-' + '=')

    # cpf = input('Digite o seu CPF(Sem pontuação): ') \
    #     .replace('.', '') \
    #     .replace('-', '') \
    #     .replace(' ', '')
    entrada = input('Digite o seu CPF(Sem pontuação): ')
    cpf = re.sub(
        r'[^0-9]',
        '',
        entrada
    )
    print(22 * '=-' + '=')
    nove_digitos = cpf[:9]
    verificação1 = 0
    verificação2 = 0

    # Primeiro validador: valida se o cpf esta sem pontuação
    if '-' not in cpf and '.' not in cpf:

        # Calculo primeiro digito
        if nove_digitos.isnumeric():
            multiplicador = 10
            soma = 0

            for digito in nove_digitos:
                soma += int(digito) * multiplicador
                multiplicador -= 1

            digito_1 = (soma * 10) % 11


                    #    'Valor' if False else 'Outro valor' if False else 'Fim'
            verificação1 = 0 if digito_1 > 9 else digito_1

            print(f'O primeiro dígito do CPF é: {verificação1}')

        dez_digitos = nove_digitos + str(digito_1)

        # calculo segundo digito
        if dez_digitos.isnumeric():
            multiplicador = 11
            soma = 0

            for digito in dez_digitos:
                soma += int(digito) * multiplicador
                multiplicador -= 1

            digito_2 = (soma * 10) % 11

            verificação2 = 0 if digito_2 > 9 else digito_2

            print(f'o segundo digito do CPF é:{verificação2}')

        digito_validador = str(digito_1) + str(digito_2)

        # Validação do CPF
        if cpf.isnumeric():
            digito_validar = cpf[9:11]

            if digito_validador == digito_validar:
                print(f'CPF:{cpf} está correto')

            else:
                print(f'CPF:{cpf} está errado, corrija o CPF!!!')
            

        else:
            print('CPF inválido. Digite somente os números.')
        
        # print(verificação1)
        # print(verificação2)
        print(f'CPF digitado:    {cpf}')
        print(f'CPF após a soma: {nove_digitos}{verificação1}{verificação2}')
        print(15 * '=-' + '=')

    else:
        print('CPF inválido. Digite somente os números.')
        print(15 * '=-' + '=')