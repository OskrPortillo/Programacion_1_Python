# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras
# y retorne dicha cantidad como un entero.

def contar_caracteres(palabra:str) -> int:
    """
    Cuenta la cantidad total de ltras que tiene la palabra dada.

    Args:
        palabra (str): La palabra a la que se le contará las letras.

    Returns:
        int: La cantidad de letras en total que tiene la palabra.
    """
    contador = 0
    for letra in palabra:
        contador += 1

    return contador


