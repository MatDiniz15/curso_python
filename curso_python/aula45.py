"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor 
iter -> me entregue seu iterador
"""
# for letra in texto

texto = 'Luiz'
# interador = iter(texto)  # iterador

# while True: 
#     try:
#         letra = next(interador)
#         print(letra)
#     except StopIteration:
#         break

for nome in texto:
    print(nome)
    




