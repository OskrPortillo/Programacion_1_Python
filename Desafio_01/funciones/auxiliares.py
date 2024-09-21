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

def  imprimir_datos_heroes(indice: int, lista_nombres: list, lista_identidades: list, 
                           lista_generos: list, lista_poderes: list, lista_alturas: list)-> str:
    
    mensaje = f"Nombre: {lista_nombres[indice]:<16} | Identidad: {lista_identidades[indice]:<22} " \
              f"| Genero: {lista_generos[indice]:<12} | Altura: {lista_alturas[indice]:<12} " \
              f"| Poder: {lista_poderes[indice]:<12} |"
    return mensaje

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
                lista_poder: list[int], lista_alturas: list[float]) -> None:
    
    if len(lista_poder) < 2:
        return lista_poder
    
    pivot = lista_poder.pop()
    numeros_menores = []
    numeros_mayores = []

    for numero in lista_poder:
        if numero <= pivot:
            numeros_menores.append(numero)
        else:
            numeros_mayores.append(numero)

    return quick_sort(numeros_menores) + pivot + quick_sort (numeros_mayores)


