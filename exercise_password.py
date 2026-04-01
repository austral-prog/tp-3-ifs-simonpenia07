def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    contraseña = str(input())
    if len(contraseña) >= 8 and  ('0' in contraseña or '1' in contraseña or '2' in contraseña or '3' in contraseña or '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or '8' in contraseña or '9' in contraseña):
        print('Contraseña valida')
    elif len(contraseña) < 8 and  ('0' in contraseña or '1' in contraseña or '2' in contraseña or '3' in contraseña or '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or '8' in contraseña or '9' in contraseña):
        print('Contraseña muy corta')
    elif len(contraseña) >= 8 and  ('0' not in contraseña and '1' not in contraseña and '2' not in contraseña and '3' not in contraseña and '4' not in contraseña and '5' not in contraseña and '6' not in contraseña and '7' not in contraseña and '8' not in contraseña and '9' not in contraseña):
        print('Debe contener un numero')
    elif len(contraseña) < 8 and  ('0' not in contraseña and '1' not in contraseña and '2' not in contraseña and '3' not in contraseña and '4' not in contraseña and '5' not in contraseña and '6' not in contraseña and '7' not in contraseña and '8' not in contraseña and '9' not in contraseña):
        print('''Contraseña muy corta
Debe contener un numero''')

