"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
while True:

    nome = input('Qual o seu nome: (caso queira sair digite "Sair") ')
    nome_corrigido = nome.title()
    nome_sem_espaço = nome_corrigido.replace(" ", "")
    letras_nome = len(nome_sem_espaço)
    #print(letras_nome)

    if letras_nome > 1:
        if letras_nome <= 4:
            print(f'O nome {nome_corrigido} é curto!')
        elif letras_nome >= 5 and letras_nome <= 6:
            print(f'O nome {nome_corrigido} é normal!')
        elif letras_nome > 6:
            print(f'O nome {nome_corrigido} é muito grande!')
        if nome_corrigido == 'Sair':
            break
    else:
        print('Digite mais de uma letra.')
