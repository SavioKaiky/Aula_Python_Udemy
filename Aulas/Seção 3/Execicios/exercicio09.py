import time
print('-=-'*10)
print(f"Calculadora simples")
print('-=-'*10)

while True:
    
    numero1 = input("Qual o primeiro número: ")

    numero2 = input("Qual o segundo número: ")

    operador = input("qual o operador para o calculo (+, -, /, *): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:

        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')    
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido.')    
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')    
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    time.sleep(2.5)
    if operador == "+":
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float )

    elif operador == "-":
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float )
    
    elif operador == "/":
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float )
    
    elif operador == "*":
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float )


    
    # print(f'O calculo {numero1} {operador} {numero2} resulta  em: {soma}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
