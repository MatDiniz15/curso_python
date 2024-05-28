"""
enumerate - enumera iteraveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'Joõa')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joõa')


for indice, nome in enumerate(lista):
    print(indice, nome)


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

