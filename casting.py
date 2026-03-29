def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = input()
    descuento = input()
    cantidad = input()
    precioconD = int(precio) - float(descuento)
    Total = float(precioconD) * int(cantidad)
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precioconD}")
    print(f"Total: {Total}")
