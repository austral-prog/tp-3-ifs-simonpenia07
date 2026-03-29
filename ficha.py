def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    Nombre = input()
    NombreS = Nombre.strip()
    NombreT = NombreS.title()
    NombreL = NombreS.lower()
    Email = input()
    Emailm = Email.lower()
    Nota1 = int(input())
    Nota2 = int(input())
    Nota3 = int(input())
    print('''========================
    FICHA DEL ALUMNO
========================''')
    print(f'Nombre: {NombreT}')
    print(f'Email: {Email.lower()}')
    print(f'Caracteres en nombre: {len(NombreT)}')
    Espacio = NombreT.find(' ')
    I_N = NombreT[0]
    I_A = NombreT[Espacio+1]
    print(f'Iniciales: {I_N}{I_A}')
    nombrem = Nombre.lower()
    EspacioU = NombreL.find(' ')
    print(f'Usuario: {NombreL[EspacioU+1:]}.{NombreL[:EspacioU]}')
    print(f"Email valido: {'@' in Email}")
    donde_arroba = Emailm.find('@')
    print(f'Dominio: {Emailm[donde_arroba+1:]}')
    print(f"Nombre para archivo: {NombreT.replace(' ','_')}")
    print(f"Cantidad de a: {NombreL.count('a')}")
    NombreI = NombreS[::-1]
    print(f'Codigo secreto: {NombreI.upper()}')
    print(f'Nota 1: {Nota1}')
    print(f'Nota 2: {Nota2}')
    print(f'Nota 3: {Nota3}')
    print(f'Suma: {Nota1 + Nota2 + Nota3}')
    print(f'Promedio: {(Nota1 + Nota2 + Nota3)/3}')
    print(f'Promedio entero: {int((Nota1 + Nota2 + Nota3)/3)}')
    print('========================')
