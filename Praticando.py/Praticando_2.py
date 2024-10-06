while True:
    Idade = input('Digite sua Idade: ')
    Altura = input('Digite su Altura: ')

    Numeros_validos = None
    Num_1_int = 0
    Num_2_float = 0

    try:
        Num_1_int = int(Idade)
        Num_2_float = float(Altura)
        Numeros_validos = True

    except:
        Numeros_validos = None

    if Num_1_int != 27 and Num_2_float != 1.83:
        print('Erro nos dados informados')

    sair = input('As informações são válidas, /'
                 'quer sair ? [s]im: ').lower().startswith('s')
    if sair is True:
        break
