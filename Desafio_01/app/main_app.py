from funciones import (
    mostrar_menu, play_sound, limpiar_pantalla,
    utn_mostrar_nombres_heroes, utn_mostrar_identidades_heroes,
    utn_mostrar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes,
    utn_filtrar_heroes_genero,
    utn_mostrar_heroes_poder_superior_promedio,
    utn_ordenar_poder_ascendente,
    utn_ordenar_altura_descendente,
    utn_ordenar_poder_a_eleccion
)

from validaciones import validar_opcion

def utn_heroes_app(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas):
    
    while True:
        
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()
        
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades)
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_alturas, lista_generos, lista_identidades, lista_nombres, lista_poder)
            case 4:
                utn_mostrar_heroes_mas_fuertes(lista_alturas, lista_generos, lista_identidades, lista_nombres, lista_poder)
            case 5:
                utn_filtrar_heroes_genero(lista_generos, lista_identidades, lista_nombres,"Femenino", "nombre")
            case 6:
                utn_filtrar_heroes_genero(lista_generos, lista_identidades, lista_nombres,"Masculino", "identidad")
            case 7:
                utn_filtrar_heroes_genero(lista_generos, lista_identidades, lista_nombres,"No-Binario", "ambos")
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lista_alturas, lista_generos, lista_identidades, lista_nombres, lista_poder)
            case 9:
                pass
            case 10: 
                utn_ordenar_poder_ascendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)
            case 11:
                utn_ordenar_altura_descendente(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)
            case 12:
                #utn_ordenar_poder_a_eleccion(lista_nombres, lista_identidades, lista_generos, lista_poder, lista_alturas)
                pass
            case 13: # Salir del programa
                break
            
        limpiar_pantalla()
        