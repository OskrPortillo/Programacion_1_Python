# 9 - Crear una función con parametros que dada una palabra y una letra, retorne 
# la cantidad de letras coincidentes que tiene esa palabra

#Opcion 1
def contar_letras_coincidentes(palabra:str, letra:str) -> int:
    """
    Cuenta la cantidad de veces que aparece una letra especifica en una palabra.

    Args:
        palabra (str): La palabra en la que se busca la letra
        letra (str): La letra que se busca en la palabra

    Returns:
        int: La cantidad de veces que aparece la letra en la palabra
    """
    contador_letra = 0
    for caracter in palabra:
        if caracter == letra:
            contador_letra += 1
    
    return contador_letra


'''
#Opcion 2

def contar_letras_coincidentes(palabra:str, letra:str) -> int:
    """
    Cuenta la cantidad de veces que aparece una letra especifica en una palabra.

    Con el método count, cuento las veces que aparece un caracter especifico en la cadena.

    Args:
        palabra (str): La palabra en la que se busca la letra
        letra (str): La letra que se busca en la palabra

    Returns:
        int: La cantidad de veces que aparece la letra en la palabra
    """
    
    return palabra.count(letra)

'''
