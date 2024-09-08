# 7 - Crear una función con parámetros que dado un número, retorne si el número es primo o no.
import Funciones_06 as multiplo

def validar_si_es_primo(numero_a_verificar: int) -> bool:
    """
    Determina si el número dado es primo.
    Esta función verifica si el número dado tiene un divisor distinto al 1 y a si mismo.

    Args:
        numero_a_verificar (int): Número que se evalua si es primo

    Returns:
        bool: Retorna True si es primo, False en caso contrario.
    """

    contador_divisores = 2
    posible_divisor = 2

    while posible_divisor < numero_a_verificar:

        if multiplo.es_multiplo(numero_a_verificar, posible_divisor):
            contador_divisores += 1
            break

        posible_divisor +=1
    
    es_primo = contador_divisores == 2
    return es_primo
