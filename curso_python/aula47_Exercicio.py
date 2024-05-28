"""
Faça um jogo para o usuario adivinhar qual a palavra secreta. 
- Voce vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, voce
vai conferir se a letra digitada está 
na palavra secreta. 
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuario. 
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_fomarda = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_fomarda += letra_secreta
        else:
            palavra_fomarda += '*'

    print('palavra_fomarda:', palavra_fomarda)

    if palavra_fomarda == palavra_secreta:
        os.system('cls') 
        print('VOCE GANHOU!! PARABENS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0 



