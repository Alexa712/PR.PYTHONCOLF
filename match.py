opcion = input('Ingresa tu opción: ')

match opcion:
    case 'fruta':
        print('seleccionaste fruta')
    case 'sopa':
        print('seleccionaste sopa')
    case _:
        print ('seleccionaste una opcipon incorrecta')