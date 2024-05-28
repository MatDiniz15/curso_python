def saudacao_com_base_na_hora():
    hora = int(input("Por favor, insira a hora (formato de 24 horas): "))
    if 0 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 18:
        return "Boa tarde"
    elif 18 <= hora <= 23:
        return "Boa noite"
    else:
        return "Hora inválida. Por favor, insira uma hora entre 0 e 23."

print(saudacao_com_base_na_hora())
