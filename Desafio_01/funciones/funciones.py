
from .auxiliares import (
    obtener_maximo, mostrar_datos_heroes,
    obtener_poder_promedio, 
    bubble_sort, selection_short, quick_sort
    )

def utn_mostrar_heroes_mas_debiles(nombres: list, identidad: list, generos: list, 
                                    poder: list, alturas: list) -> None:
    """
    Función que calcula el poder maximo entre los heroes y
    muestra los heroes que esten por debajo de ese poder.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """
     
    maximo_poder = obtener_maximo(poder)
    mitad_maximo_poder = maximo_poder / 2
    print(f"\nLa mitad del maximo poder entre los heroes es: {mitad_maximo_poder}")
    
    for indice in range(len(poder)):
        if poder[indice] < mitad_maximo_poder:
            mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre", "poder"])

def utn_mostrar_heroes_poder_superior_promedio(nombres: list, identidad: list, generos: list, 
                                               poder: list, alturas: list) -> None:
    """
    Función que calcula el poder promedio entre los heroes y
    muestra los heroes que igualan o superan ese poder.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """


    poder_promedio = obtener_poder_promedio(poder)
    print(f"\nEl poder promedio entre los heroes es: {poder_promedio:4.2f}")

    for indice in range(len(poder)):
        if poder[indice] >= poder_promedio:
            mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre", "poder"])


def utn_filtrar_heroes_genero(nombres: list, identidad: list, generos: list, poder: list, 
                              alturas: list, tipo_genero: str, info_heroe: str)-> None:
    """
    Filtra y muestra información de los héroes según el género especificado.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
        tipo_genero (str):   Género por el cual se desea filtrar. 
                             Puede ser "Femenino", "Masculino" o "No-Binario".
        info_heroe (str): Especifica qué información del héroe se desea mostrar.
                          - "nombre": Muestra solo el nombre del héroe.
                          - "identidad": Muestra solo la identidad del héroe.
                          - "ambos": Muestra el nombre y la identidad del héroe.
    """

    for indice in range(len(generos)):
        
        if generos[indice] == tipo_genero:
            if info_heroe == "nombre":
                mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas, ["nombre"])
            elif info_heroe == "identidad":
                mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas, ["identidad"])
            elif info_heroe == "ambos":
                mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre", "identidad"])
                      

def utn_mostrar_heroes_mas_fuertes(nombres: list, identidad: list, generos: list, 
                                   poder: list, alturas: list) -> None:
    """
    Función que recibe varias listas con información de heroes y muestra 
    los datos completos del o los héroe que tienen mayor poder. 

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """
    mayor_poder = obtener_maximo(poder)

    for indice in range(len(poder)):
        
        if poder[indice] == mayor_poder:
            mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre", "identidad", "genero", "poder", "altura"])


def utn_mostrar_heroe_mayor_altura(nombres: list, identidad: list, generos: list, 
                                   poder: list, alturas: list) -> None:
    """
    Función que recibe varias listas que contienen información de héroes y 
    muestra los datos completos del héroe que tiene la mayor altura.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """
    
    mayor_altura = obtener_maximo(alturas)

    for indice in range(len(alturas)):
        
        if alturas[indice] == mayor_altura:
            mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre", "identidad", "genero", "poder", "altura"])


def utn_mostrar_identidades_heroes(nombres: list, identidad: list, generos: list, 
                                   poder: list, alturas: list) -> None:
    """
    Función que recibe varias lista con información de los heroes 
    y muestra unicamente la identidad de los heroes.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """
    for indice in range(len(identidad)):
        mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["identidad"])


def utn_mostrar_nombres_heroes(nombres: list, identidad: list, generos: list, 
                               poder: list, alturas: list) -> None:
    """
    Función que recibe varias lista con información de los heroes 
    y muestra unicamente los nombres de los heroes.

    Args:
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
    """
    for indice in range(len(nombres)):
        mostrar_datos_heroes(indice, nombres, identidad, generos, poder, alturas,
                                 ["nombre"])

           

def utn_ordenar_poder_ascendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) -> None:
    
    selection_short(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, True)
    
    for indice in range(len(lista_poder)):
        mostrar_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, 
                             ["nombre", "identidad", "genero", "poder", "altura"])

def utn_ordenar_altura_descendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) ->None:
    
    bubble_sort(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, False)
    
    for indice in range(len(lista_alturas)):
        mostrar_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, 
                             ["nombre", "identidad", "genero", "poder", "altura"])

def utn_ordenar_poder_a_eleccion(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas) ->None:
    ordenamiento = "ASC"
    quick_sort(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, ordenamiento)

    for indice in range(len(lista_poder)):
        mostrar_datos_heroes(indice, lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas, 
                            ["nombre", "identidad", "genero", "poder", "altura"])
    

