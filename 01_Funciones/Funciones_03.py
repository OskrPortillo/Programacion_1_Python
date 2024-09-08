# 3 - Crear una función que dado un parametro que corresponde a un nombre, salude.

def saludar(nombre: str) -> None:
    """
    Saluda al nombre que ingresa por parámetro.
    Args:
        nombre (str): Nombre de la persona a saludar.
    """
    
    print(f"Hola {nombre}") 


nombre_a_saludar = "Oscar"
saludar(nombre_a_saludar)