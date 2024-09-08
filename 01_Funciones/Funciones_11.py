# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego
# calculará cual de ellas tiene mayor cantidad de letras y tendra que imprimirla en consola
# junto con la cantidad de letras que posee

import Funciones_10 as letrastotal

def palabra_mayor_longitud(palabra_uno:str, palabra_dos:str, palabra_tres:str) -> None:
    """
    Determina entre 3 palabras la que tiene mayor cantidad de letras.

    letrastotal es un modulo que tiene la funcion de contar letras de una palabra

    Args:
        palabra_uno (str): La primera palabra a evaluar
        palabra_dos (str): La segunda palabra a evaluar
        palabra_tres (str): La tercera palabra a evaluar
    """
    mayor_palabra = palabra_uno

    if letrastotal.contar_letras_total(palabra_dos) > letrastotal.contar_letras_total(mayor_palabra):
        mayor_palabra = palabra_dos
    
    if letrastotal.contar_letras_total(palabra_tres) > letrastotal.contar_letras_total(mayor_palabra):
        mayor_palabra = palabra_tres

    cantidad_letras = letrastotal.contar_letras_total(mayor_palabra)    
    print(f"La palabra con mayor cantidad de letras es {mayor_palabra} con {cantidad_letras} letras") 
