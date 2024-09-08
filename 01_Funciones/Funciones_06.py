# 6 - Crear una función con parámetros que dado dos número, retorne True si son multiplos, 
# False caso contrario.

def es_multiplo(dividendo: int, divisor: int) -> bool:
    """
    Verifica si los dos numeros enteros que ingresaron por parámetro 
    son multiplos

    Args:
        dividendo (int): Número entero que se va a dividir.
        divisor (int): Número entero que va a dividir al dividendo.

    Returns:
        bool: Retorna True si los números son multiplo, False en caso contrario
    """
    check_multiplo = dividendo % divisor == 0
    return check_multiplo


