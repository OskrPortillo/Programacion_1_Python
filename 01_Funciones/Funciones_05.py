# 5 - Crear una funcion con parámetros que dado un radio, calcule el area de un círculo

import math

def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el area de un círculo dado su radio

    Utiliza el módulo math para usar la constante matemática pi

    Args:
        radio (float): El radio del círculo

    Returns:
        float: El área del círculo usando la fórmula A = π * (r * r).
    """
    area_circulo = math.pi * (radio * radio)
    print(f"El circulo de radio {radio} tiene un area de area {area_circulo}")
