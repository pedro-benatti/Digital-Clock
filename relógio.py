horario= input('Digite que horas são: ')

if horario.isdigit():
    horario=int(horario)
    if horario <0 and horario > 23:
        print('Insira horas entre 0 e 23!')

    if horario <=11:
        print('Bom dia!')
    elif horario <=17:
        print('Boa tarde!')
    else:
        print('Boa noite')


else:
    print('ERROR, insira um horário válido!!')