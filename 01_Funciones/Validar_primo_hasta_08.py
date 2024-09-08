# 8 - Crear una función con parámetros que dado un número, recorra todos los números anteriores
# y  muestre cual de ellos es número primo y cual no lo es.

import Validar_numero_primo_07

def verificar_numeros_primos_hasta(numero_tope_a_verificar: int) -> None:
    """
    Verifica si todos los numeros anteriores al dado, incluido este, son primos o no. 
    Y los imprime. 

    Args:
        numero_tope_a_verificar (int): Número hasta donde se evaluara si son primos o no.
    """

    for numero in range (2, numero_tope_a_verificar+1):

        if Validar_numero_primo_07.validar_si_es_primo(numero):
            print(f"{numero} es primo")
        else:
            print((f"{numero} no es primo"))

