"""
Exercicio
Exiba os indices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Gregory')
lista.append('Dior')
lista.append('Mayara')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
