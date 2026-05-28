import os
lista_compra = []
while True:
    try:
        os.system('cls')
        print('=-=-=-=-= Menu =-=-=-=-=')
        print('1 - Adcionar item\n2 - Editar lista\n3 - Mostrar lista\n4 - Sair')
        n1 = int(input('Escolha uma opção: '))
        if n1 == 1:
            os.system('cls')
            print('=-=-=-=-= Adcionar item =-=-=-=-=')
            item_adc = input('digite o item: ')
            lista_compra.append(item_adc)

        elif n1 == 2:
            while True:
                os.system('cls')
                print('=-=-=-=-= Editar lista =-=-=-=-=')
                print('=-=-=-=-= Lista =-=-=-=-=')
                if lista_compra == []:
                    print('A lista está vasia!!')
                else:
                    for i, item in enumerate(lista_compra):
                        print(f'{i} - {item}')
                print(20*'=-' + '=')
                print('1 - Editar\n2 - Apagar item\n3 - Limpar lista\n4 - Menu principal')
                n2 = int(input('Excolha uma opção: '))
                
                while True:
                    if n2 == 1:
                        os.system('cls')
                        print('=-=-=-=-= Lista =-=-=-=-=')
                        if lista_compra == []:
                            print('A lista está vasia!!')
                            _ = input('Para seguir aperte o enter:')
                            break
                        else:
                            for i, item in enumerate(lista_compra):
                                print(f'{i} - {item}')
                        print('=-=-=-=-= Editar =-=-=-=-=')
                        indice = int(input('Digite o indice: '))
                        novo_valor = input(f'Digite o novo valor para o item {indice}: ')
                        lista_compra[indice] = novo_valor
                        break

                    elif n2 == 2:
                        os.system('cls')
                        print('=-=-=-=-= Lista =-=-=-=-=')
                        if lista_compra == []:
                            print('A lista está vasia!!')
                            _ = input('Para seguir aperte o enter:')
                            break
                        else:
                            for i, item in enumerate(lista_compra):
                                print(f'{i} - {item}')
                        print('=-=-=-=-= Apagar Item =-=-=-=-=')
                        indice = input('Digite o indice: ')
                        try:
                            del lista_compra[indice]
                            break
                        except ValueError:
                            print('Por favor digite um número inteiro')
                            _ = input('Para seguir aperte o enter:')
                        except IndexError:
                            print('Indice não existe na lista')
                            _ = input('Para seguir aperte o enter:')
                        except Exception:
                            print('Erro: 404\n Erro desconhecido')
                            _ = input('Para seguir aperte o enter:')

                    elif n2 == 3:
                        os.system('cls')
                        print('=-=-=-=-= Limpar lista =-=-=-=-=')
                        lista_compra.clear()
                        print('A lista foi limpa, Agora vc pode adicionar novos valores!')
                        _ = input('Para seguir aperte o enter:')
                        break

                    elif n2 == 4:
                        break
                        
                    else:
                        os.system('cls')
                        print('Valor inexistente! Tente novamente outro valor')
                        _ = input('Para seguir aperte o enter:')
                
                break

        elif n1 == 3:
            os.system('cls')
            print('=-=-=-=-= Lista =-=-=-=-=')

            if lista_compra == []:
                print('A lista está vasia!!')
            
            for i, item in enumerate(lista_compra, start=(1)):
                print(f'{i} - {item}')
            
            n3 = input('Deseja voltar ao menu principal: [S]im ou [N]ão ')
            if n3 == 'S':
                break
            else:
                continue
        elif n1 == 4:
            break
        else:
            os.system('cls')
            print('Valor inexistente')
            _ = input('Para seguir aperte o enter:')
    except ValueError:
        print(16*'=-' + '=')
        print('Por favor digite um número inteiro')
        _ = input('Para seguir aperte o enter:')
    except KeyboardInterrupt:
        break
    except Exception:
        os.system('cls')
        print(16*'=-' + '=')
        print('Erro: 404\nErro desconhecido')
        _ = input('Para seguir aperte o enter:')
        continue