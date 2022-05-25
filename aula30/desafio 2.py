print('SAUDAÇÃO CONFORME HORÁRIO DO DIA')

horário = input('Digite um horário (0-23): ')
if horário.isdigit():
    horário = int(horário)

    if horário < 0 or horário > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if horário <= 11:
            print('Bom dia!')
        elif horário <=17:
            print('Boa tarde')
        else:
            print('Boa noite!')
