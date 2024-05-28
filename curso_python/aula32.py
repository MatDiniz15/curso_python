"""
Faça um, programa que peça ao usuario para digitar um numero interio, 
informe se este numero é par ou impar. Caso o usario não digite um numero 
inteiro, informe que não é um numero inteiro. 
"""

#entrada = input('Digite um número: ')

#if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')

#else:
#     print('Você não digitou um número inteiro')

#try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
#except:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#entrada = input('Digite a hora em números inteiros: ')

#try:
#    hora = int(entrada)

#    if hora >= 0 and hora <= 11:
#       print('Bom dia')
#    elif hora >= 12 and hora <= 17:
#        print('Boa tarde')
#    elif hora >= 18 and hora <= 23:
#        print('Boa noite')
#    else: 
#        print('Não conheço essa hora')
#except:
#    print('Por favor, digite apenas numeros inteiros')

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto", se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')