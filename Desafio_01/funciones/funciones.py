
from .auxiliares import obtener_maximo, imprimir_datos_heroes

def utn_mostrar_nombres_heroes(lista_nombres: list) -> None:
    """
    Esta funcion recibe una lista y muestra los nombres de los heroes.

    Args:
        lista_nombres (list): Lista de strings
    """
    for nombre in lista_nombres:
        print(nombre)

def utn_mostrar_identidades_heroes(lista_identidades: list)->None:
    for nombre in lista_identidades:
        print(nombre)

def utn_mostrar_heroe_mayor_altura(lista_alturas: list, lista_generos: list, lista_identidades: list,
                                    lista_nombres: list, lista_poder: list)-> None:
    """
    Esta función recibe varias listas que contienen información de héroes y muestra 
    los datos completos del héroe que tiene la mayor altura.

    Args:
        lista_alturas (list): lista de float
        lista_generos (list): _lista de strings
        lista_identidades (list): lista de strings
        lista_nombres (list): lista de strings
        lista_poder (list): lista de int
    """
    
    mayor_altura = obtener_maximo(lista_alturas)
    for indice in range(len(lista_alturas)):
        if lista_alturas[indice] == mayor_altura:
            imprimir_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)
    
    