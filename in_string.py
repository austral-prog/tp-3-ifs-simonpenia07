def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input()
    nombremin = nombre.lower()
    contienea = 'a' in nombremin
    print(f'Contiene a: {contienea}')
    contienee = 'e' in nombremin
    print(f'Contiene e: {contienee}')
    contienei = 'i' in nombremin
    print(f'Contiene i: {contienei}')
    contieneo = 'o' in nombremin
    print(f'Contiene o: {contieneo}')
    contieneu = 'u' in nombremin
    print(f'Contiene u: {contieneu}')
