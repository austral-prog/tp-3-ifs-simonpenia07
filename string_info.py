def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f'Palabra: {palabra}')
    longitud = len(palabra)
    print(f'Longitud: {longitud}')
    PL = palabra[0]
    print(f'Primera letra: {PL}')
    UL = palabra[-1]
    print(f'Ultima letra: {UL}')
    P3 = palabra * 3
    print(f'Repetida: {P3}')
    print(f'Decorada: ***{palabra}***')
