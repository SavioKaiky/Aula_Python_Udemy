from random import randint
nove_digitos = ''

for i in range(9):
    nove_digitos += str(randint(0, 9))


# Calculo primeiro digito
if nove_digitos.isnumeric():
    multiplicador = 10
    soma = 0

    for digito in nove_digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    digito_1 = (soma * 10) % 11


            #    'Valor' if False else 'Outro valor' if False else 'Fim'
    digito_verificado_1 = 0 if digito_1 > 9 else digito_1

    # print(f'O primeiro dígito do CPF é: {digito_verificado_1}')

dez_digitos = nove_digitos + str(digito_verificado_1)
digito_verificado_1 = str(digito_verificado_1)

# calculo segundo digito
if dez_digitos.isnumeric():
    multiplicador = 11
    soma = 0

    for digito in dez_digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    digito_2 = (soma * 10) % 11

    digito_verificado_2 = 0 if digito_2 > 9 else digito_2
    digito_verificado_2 = str(digito_verificado_2)

    # print(f'o segundo digito do CPF é:{digito_verificado_2}')


else:
    print('CPF inválido. Digite somente os números.')


    
print(nove_digitos + digito_verificado_1 + digito_verificado_2)