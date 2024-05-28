"""
Listas em Python 
Tipo list - Mutavel
Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento 
Métodos uteis: append, insert, pop, del, clear, extend, + 
"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # false
# print(lista, type(lista))


#         0     1     2            3    4
#        -5    -4    -3           -2   -1
lista = [123, True, 'Luiz Otavio', 1.2, []]
lista[-3] = 'Matheus'
print(lista)
print(lista[2], type(lista[2]))