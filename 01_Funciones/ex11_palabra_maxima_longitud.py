# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego
# calculará cual de ellas tiene mayor cantidad de letras y tendra que imprimirla en consola
# junto con la cantidad de letras que posee

import ex10_contar_caracteres

def validar_palabra()-> str:
    palabra = None

    while not palabra or not palabra.isalpha():
        palabra = input("Ingrese una palabra (solo letras): ")

    return palabra

def palabra_mas_larga() -> None:
    """
    Determina entre 3 palabras la que tiene mayor cantidad de letras.

    """
    palabra_mayor = None
    contador_mayor = 0

    for _ in range(3):
        string = validar_palabra()

        cantidad_caracter = ex10_contar_caracteres.contar_caracteres(string)
        print(cantidad_caracter)

        if not palabra_mayor or cantidad_caracter > contador_mayor:
            contador_mayor = cantidad_caracter
            palabra_mayor = string

    print(f"La palabra {palabra_mayor} es la que tiene mayor cantidad de letras con {contador_mayor}")