def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    Base = input()
    Altura = input()
    BaseE = int(Base)
    AlturaE = int(Altura)
    print(f"Base: {BaseE}")
    print(f"Altura: {AlturaE}")
    area = BaseE * AlturaE
    print(f"Area: {area}")
    Perimetro = BaseE * 2 + AlturaE * 2
    print(f"Perimetro: {Perimetro}")
