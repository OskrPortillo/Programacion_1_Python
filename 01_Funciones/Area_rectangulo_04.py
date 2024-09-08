# 4 - Crear una función que dado una base y un altura, calcule el area de un rectángulo.

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de de un rectángulo

    Args:
        base (flotat): La base del rectángulo
        altura (float): La altura del rectángulo

    Returns:
        float: El area del rectángulo
    """
    area = base * altura
    print(f"El area del rectangulo es {area}")


