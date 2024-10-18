"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

import os

inserir = '[i]nserir'
apagar = '[a]pagar'
listar = '[l]istar'
lista = []


while True:

    opcoes = input('Selecione uma opção:'f'{inserir}, {apagar}, {listar}: ')

    if opcoes == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print('Item listado.')

    elif opcoes == 'a':
        os.system('cls')
        indice_str = input(
            'Escolha o ìndice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número int')
        except IndexError:
            print('O ìndice não existe ou já foi apagado.')
        except Exception:
            print('Erro desconhecido.')

    elif opcoes == 'l':
        os.system('cls')
        print('Lista de Compras: ')

    else:
        print('Por favor coloque uma das opções.')

    if len(lista) == 0:
        print('Nada para listar')

    for i, valor in enumerate(lista):
        print(i, valor)
