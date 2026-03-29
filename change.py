def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = input()
    print(float(gasto))
    print("Dinero recibido")
    dinero = input()
    print(dinero)
    print()
    print('Vuelto')
    print()
    print('Pesos:')
    vueltoP = float(dinero) - float(gasto)
    vuelto_entero = int(vueltoP)
    print(vuelto_entero)
    vuelto_centavos = float(vueltoP) - int(vueltoP)
    print('Centavos:')
    print(round(vuelto_centavos * 100))

