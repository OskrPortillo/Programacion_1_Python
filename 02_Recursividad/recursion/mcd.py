
def mcd(numero_a: int, numero_b: int) -> int:
    if numero_b == 0:
        return numero_a
    else:
        modulo_a_b = numero_a % numero_b
        return mcd(numero_b, modulo_a_b)


maximo_comun_divisor = mcd(5, 10)
print(maximo_comun_divisor)