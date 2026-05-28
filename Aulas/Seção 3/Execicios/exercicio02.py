# o codigo vai pedir os dados do usuario
nome = str(input('Qual o seu nome: ')).title()
altura =  float(input('Qual a sua altura: '))
peso = float(input('Qual o seu peso: '))

# O codigo vai fazer o calculo do imc coproral do usuario
imc = peso / (altura ** 2)

# O codigo agora vai imprimir na tela o resultado do calculo e algumas informações do usuario
print(f'{nome} tem {altura:.2f} metros de altura,\nEle(a) pesa {peso:.2f} e seu IMC é de: {imc:.2f}')
if imc <= 18.5:
    print('Voce está muito abaixo do peso')
elif imc > 18.5 and imc < 24.9:
    print('Você está com o peso normal')
elif imc > 25 and imc < 29.9:
    print('Você está com sobrepeso')
elif imc > 30 and imc < 34.9:
    print('Você está com obesidade grau I')
elif imc > 35 and imc < 39.9:
    print('Você está com obesidade grau II')
elif imc > 40:
    print('Voce está com obesidade grau III')