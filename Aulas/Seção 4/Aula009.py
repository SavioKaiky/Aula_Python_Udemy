"""
Closure e funções que retornam outras funçoes
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

retornar_bom_dia = criar_saudacao('Bom dia')
retornar_boa_noite = criar_saudacao('Boa noite')

# print(s1)
# print(s2())

lista_nomes =['Maria', 'Jorge', 'Luiz', 'Joana']

for nome in lista_nomes:
    print(retornar_bom_dia(nome))
    print(retornar_boa_noite(nome))
