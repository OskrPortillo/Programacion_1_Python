
from .auxiliares import (
    obtener_maximo, imprimir_datos_heroes,
    obtener_poder_promedio, 
    bubble_sort, selection_short, quick_sort
    )

def utn_mostrar_heroes_poder_superior_promedio(alturas: list, generos: list, identidades: list, 
                                                nombres: list, poder: list) -> None:
    
    poder_promedio = obtener_poder_promedio(poder)
    print(poder_promedio)

    for indice in range(len(poder)):
        if poder[indice] >= poder_promedio:
            print(imprimir_datos_heroes(indice, nombres, identidades, generos, poder, alturas))


def utn_filtrar_heroes_genero(lista_generos: list, lista_identidades: list, 
                              lista_nombres: list, genero: str, info_heroe: str)-> None:
    """
    Filtra y muestra información de los héroes según el género especificado.

    Args:
        generos (list): lista de strings
        identidades (list): lista de strings
        nombres (list): lista de strings
        genero (str):   Género por el cual se desea filtrar. 
                        Puede ser "Femenino", "Masculino" o "No-Binario".
        info_heroe (str): Especifica qué información del héroe se desea mostrar.
                          - "nombre": Muestra solo el nombre del héroe.
                          - "identidad": Muestra solo la identidad del héroe.
                          - "ambos": Muestra el nombre y la identidad del héroe.
    """

    for indice in range(len(lista_generos)):
        
        if lista_generos[indice] == genero:
            if info_heroe == "nombre":
                print(f"Nombre: {lista_nombres[indice]}")
            elif info_heroe == "identidad":
                print(f"Identidad: {lista_identidades[indice]}")
            elif info_heroe == "ambos":
                print(f"Nombre: {lista_nombres[indice]}, Identidad: {lista_identidades[indice]}")
                      

def utn_mostrar_heroes_mas_fuertes(alturas: list, generos: list, identidades: list, 
                                   nombres: list, poder: list)-> None:
    """
    Función que recibe varias listas con información de heroes y muestra 
    los datos completos del o los héroe que tienen mayor poder. 

    Args:
        alturas (list): lista de float
        generos (list): _lista de strings
        identidades (list): lista de strings
        nombres (list): lista de strings
        poder (list): lista de int
    """
    mayor_poder = obtener_maximo(poder)

    for indice in range(len(poder)):
        
        if poder[indice] == mayor_poder:
            print(imprimir_datos_heroes(indice, nombres, identidades, generos, poder, alturas))


def utn_mostrar_heroe_mayor_altura(alturas: list, generos: list, identidades: list,
                                    nombres: list, poder: list)-> None:
    """
    función recibe varias listas que contienen información de héroes y muestra 
    los datos completos del héroe que tiene la mayor altura.

    Args:
        alturas (list): lista de float
        generos (list): _lista de strings
        identidades (list): lista de strings
        nombres (list): lista de strings
        poder (list): lista de int
    """
    
    mayor_altura = obtener_maximo(alturas)

    for indice in range(len(alturas)):
        
        if alturas[indice] == mayor_altura:
            print(imprimir_datos_heroes(indice, nombres, identidades, generos, poder, alturas))


def utn_mostrar_identidades_heroes(identidades: list)->None:
    """
    Esta funcion recibe una lista y muestra las identidades de los heroes.

    Args:
        identidades (list): Lista de strings
    """
    for id in identidades:
        print(id)


def utn_mostrar_nombres_heroes(nombres: list) -> None:
    """
    Esta funcion recibe una lista y muestra los nombres de los heroes.

    Args:
        nombres (list): Lista de strings
    """
    for nombre in nombres:
        print(nombre)

           

def utn_ordenar_poder_ascendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) -> None:
    
    selection_short(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, True)
    
    for indice in range(len(lista_poder)):
        print(imprimir_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas))

def utn_ordenar_altura_descendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) ->None:
    
    bubble_sort(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, False)
    
    for indice in range(len(lista_alturas)):
        print(imprimir_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas))

def utn_ordenar_poder_a_eleccion(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) ->None:

    quick_sort(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)

    for indice in range(len(lista_poder)):
        imprimir_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)
    

