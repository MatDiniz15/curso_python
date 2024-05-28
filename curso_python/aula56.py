"""
split e join com list e str 
split - divide um string (list)
join - une uma string 
"""

frase = 'Olha só que, coisa interessante'
lista_frase_crua = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())


# print(lista_frase_crua)
# print(lista_frase)
frases_unidas = ', '.join(lista_frase)
print(frases_unidas)