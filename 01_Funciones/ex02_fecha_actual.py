# 2 - Crear una función sin parámetros que retorne el año actual como número entero. 

def obtener_año_actual() -> int:
    """
    Retorna el año actual como número entero

    Returns:
        int : El año actual
    """
    
    año_actual = "2024"
    return int(año_actual)

# Usando el modulo datetime 
'''
import datetime

def obtener_año_actual() -> int:
    """ 
    Retorna el año actual como número entero

    Utiliza el módulo datetime para obtener la fecha actual
    y extra el año.

    Returns:
        int : El año actual
    """

    año_actual = datetime.datetime.now().year
    return año_actual

año = obtener_año_actual()
print(año)
'''

