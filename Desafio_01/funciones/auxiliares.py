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
    mixer.music.load('./assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

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

def  imprimir_datos_heroes(indice: int, lista_nombres: list, lista_identidades: list, lista_generos: list, lista_poderes: list, lista_alturas: list)-> None:
    print(f"{lista_nombres[indice]:15} | {lista_identidades[indice]:25} | {lista_generos[indice]:10} \
          | {lista_alturas[indice]:4} | {lista_poderes[indice]:4}")


