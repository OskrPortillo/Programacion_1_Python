# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time


def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load('./Desafio_01/assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)


def obtener_poder_promedio(lista_poder: list) -> float:
    """
    Función que recibe una lista y calcula el promedio.

    Args:
        lista_poder (list): lista de enteros

    Returns:
        float: El promedio de los valores de la lista.
    """
    suma_poder = 0
    for indice in range(len(lista_poder)):
        suma_poder += lista_poder[indice]

    promedio = suma_poder / len(lista_poder)
    return promedio


def mostrar_datos_heroes(i: int, lista_nombres, lista_identidad: list, lista_generos: list, 
                         lista_poderes: list, lista_alturas: list, dato_a_imprimir: list[str])-> None:
    """
    Funcion que muestra la información de un héroe según el índice 
    y que dato especifico quiero que muestre.

    Args:
        i (int): El índice del héroe dentro de las listas.
        nombres (list): lista de strings
        identidad (list): lista de strings
        generos (list): lista de strings
        poder (list): lista de enteros
        alturas (list): lista de floats
        dato_a_imprimir (list[str]): lista de los dato a imprimir. Puede incluir "nombres", "identidades",
                                    "generos", "poderes", "alturas".
    """
    
    mensaje = ""

    for dato in dato_a_imprimir:
        match dato:
            case "nombre":
                mensaje += f"Nombre: {lista_nombres[i]:<16} | "
            case "identidad":
                mensaje += f"Identidad: {lista_identidad[i]:<32} | "
            case "genero":
                mensaje += f"Genero: {lista_generos[i]:<12} | "
            case "poder":
                mensaje += f"Poder: {lista_poderes[i]:<12} | "
            case "altura":
                mensaje += f"Altura: {lista_alturas[i]:<12} | "
            case _:
                print(f"Dato '{dato}' no es válida.")
    
    print(mensaje)


def obtener_maximo(lista_numeros: list) -> float:
    """
    Función para obtener el número más grande de una lista 
    y retornarlo como flotante.

    Args:
        lista_numeros (list):  Lista de números (enteros o flotantes) 
        de la cual se obtendrá el valor máximo. 

    Returns:
        float: El número más grande de la lista, convertido a flotante.
    """
    maximo = None
    for numero in lista_numeros:
        if maximo is None or numero > maximo:
            maximo = numero
        
    return float(maximo)


def bubble_sort(lista_nombres: list[str], lista_identidades: list[str],lista_generos: list [str], \
                lista_poder: list[int], lista_alturas: list[float], orden_ascendente :bool) ->None:

    for indice in range(len(lista_alturas)-1):
        for sub_indice in range(indice + 1, len(lista_alturas)):

            if orden_ascendente:    
                if lista_alturas[indice] > lista_alturas[sub_indice]:
                    lista_alturas[indice], lista_alturas[sub_indice] =\
                    lista_alturas[sub_indice], lista_alturas[indice]

                    lista_poder[indice], lista_poder[sub_indice] =\
                    lista_poder[sub_indice], lista_poder[indice]

                    lista_generos[indice], lista_generos[sub_indice] =\
                    lista_generos[sub_indice], lista_generos[indice]

                    lista_identidades[indice], lista_identidades[sub_indice] =\
                    lista_identidades[sub_indice], lista_identidades[indice]

                    lista_nombres[indice], lista_nombres[sub_indice] =\
                    lista_nombres[sub_indice], lista_nombres[indice]
            else: #descendente
                    if lista_alturas[indice] < lista_alturas[sub_indice]:
                        lista_alturas[indice], lista_alturas[sub_indice] =\
                        lista_alturas[sub_indice], lista_alturas[indice]

                        lista_poder[indice], lista_poder[sub_indice] =\
                        lista_poder[sub_indice], lista_poder[indice]

                        lista_generos[indice], lista_generos[sub_indice] =\
                        lista_generos[sub_indice], lista_generos[indice]

                        lista_identidades[indice], lista_identidades[sub_indice] =\
                        lista_identidades[sub_indice], lista_identidades[indice]

                        lista_nombres[indice], lista_nombres[sub_indice] =\
                        lista_nombres[sub_indice], lista_nombres[indice]
                
def selection_short(lista_nombres: list[str], lista_identidades: list[str],lista_generos: list [str], \
                lista_poder: list[int], lista_alturas: list[float], orden_ascendente: bool) -> None:
            
    for indice in range (len(lista_poder) - 1):
        indice_minimo_o_maximo = indice

        for sub_indice in range(indice + 1, len(lista_poder)):

            if orden_ascendente:
                if lista_poder[sub_indice] < lista_poder[indice_minimo_o_maximo]:
                    indice_minimo_o_maximo = sub_indice
            else:
                if lista_poder[sub_indice] > lista_poder[indice_minimo_o_maximo]:
                    indice_minimo_o_maximo = sub_indice
        
        if indice_minimo_o_maximo != indice:
            lista_poder[indice], lista_poder[indice_minimo_o_maximo] =\
            lista_poder[indice_minimo_o_maximo], lista_poder[indice]

            lista_alturas[indice], lista_alturas[indice_minimo_o_maximo] =\
            lista_alturas[indice_minimo_o_maximo], lista_alturas[indice]

            lista_generos[indice], lista_generos[indice_minimo_o_maximo] =\
            lista_generos[indice_minimo_o_maximo], lista_generos[indice]

            lista_identidades[indice], lista_identidades[indice_minimo_o_maximo] =\
            lista_identidades[indice_minimo_o_maximo], lista_identidades[indice]

            lista_nombres[indice], lista_nombres[indice_minimo_o_maximo] =\
            lista_nombres[indice_minimo_o_maximo], lista_nombres[indice]


def quick_sort(lista_nombres: list[str], lista_identidades: list[str],lista_generos: list [str], \
                lista_poder: list[int], lista_alturas: list[float], modo: str) -> None:
    
    if len(lista_poder) < 2:
        return lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas
    
    pivot_poder = lista_poder.pop()
    pivot_nombre = lista_nombres.pop()
    pivot_identidad = lista_identidades.pop()
    pivot_genero = lista_generos.pop()
    pivot_altura = lista_alturas.pop()
    
    poder_menores, nombre_menores, identidad_menores, genero_menores, altura_menores = [], [], [], [], []
    poder_mayores, nombre_mayores, identidad_mayores, genero_mayores, altura_mayores = [], [], [], [], []

    for i in range(len(lista_poder)):
        if lista_poder[i] <= pivot_poder:
            poder_menores.append(lista_poder[i])
            nombre_menores.append(lista_nombres[i])
            identidad_menores.append(lista_identidades[i])
            genero_menores.append(lista_generos[i])
            altura_menores.append(lista_alturas[i])
        else:
            poder_mayores.append(lista_poder[i])
            nombre_mayores.append(lista_nombres[i])
            identidad_mayores.append(lista_identidades[i])
            genero_mayores.append(lista_generos[i])
            altura_mayores.append(lista_alturas[i])

    if modo == "ASC":
        izquierda_poder, derecha_poder = poder_menores, poder_mayores
        izquierda_nombre, derecha_nombre = nombre_menores, nombre_mayores
        izquierda_identidad, derecha_identidad = identidad_menores, identidad_mayores
        izquierda_genero, derecha_genero = genero_menores, genero_mayores
        izquierda_altura, derecha_altura = altura_menores, altura_mayores
    else:  # Para "DESC"
        izquierda_poder, derecha_poder = poder_mayores, poder_menores
        izquierda_nombre, derecha_nombre = nombre_mayores, nombre_menores
        izquierda_identidad, derecha_identidad = identidad_mayores, identidad_menores
        izquierda_genero, derecha_genero = genero_mayores, genero_menores
        izquierda_altura, derecha_altura = altura_mayores, altura_menores


    return quick_sort(izquierda_nombre, izquierda_identidad, izquierda_genero, izquierda_poder, izquierda_altura, modo) \
          + pivot_poder + quick_sort (derecha_nombre, derecha_identidad, derecha_genero, derecha_poder, derecha_altura, modo)


