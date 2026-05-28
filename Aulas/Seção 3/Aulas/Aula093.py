''' Imprecisão de ponto flutuante
 print(0.1 + 0.1 + 0.1 - 0.3)'''

'''primeira forma de resolver a imprecisão'''
n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print('Primeira resolução:')
print(n3)
print(f'{n3:.2f}')

'''segunda forma de resolver a imprecisão'''
n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print('Segunda resolução:')
print(n3)
print(round(n3, 2))

'''terceira forma de resolver a imprecisão'''
import decimal

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3 = n1 + n2
print('Terceira resolução:')
print(n3)