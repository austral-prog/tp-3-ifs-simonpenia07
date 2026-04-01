def compare():
    """
    Ejercicio 4 - Comparar Dos Números

    Leer dos números enteros mediante input(). Compararlos e imprimir si el primero
    es mayor, menor o igual al segundo.

    Ejemplo:
        Para las entradas "10" y "5", la salida esperada es:
        10 es mayor que 5

        Para las entradas "3" y "8", la salida esperada es:
        3 es menor que 8

        Para las entradas "7" y "7", la salida esperada es:
        7 es igual a 7
    """
    Numero1 = int(input())
    Numero2 = int(input())
    if Numero1 > Numero2:
        print(f'{Numero1} es mayor que {Numero2}')
    if Numero1 < Numero2:
        print(f'{Numero1} es menor que {Numero2}')
    else:
        print(f'{Numero1} es igual a {Numero2}')
