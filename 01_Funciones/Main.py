import ex01_bienvenida
import ex02_fecha_actual
import ex03_saludo
import ex04_area_rectangulo
import ex05_area_circulo
import ex06_multiplo
import ex07_validar_primo
import ex08_validar_primo_hasta
import ex09_contar_caracter_igual
import ex10_contar_caracteres
import ex11_palabra_maxima_longitud

print("Ejericio 1")
ex01_bienvenida.bienvenida()

print("\nEjercicio 2")
anio_actual = ex02_fecha_actual.obtener_año_actual()
print(f"El año actual es {anio_actual}")

print("\nEjercicio 3")
ex03_saludo.saludar("Oscar")

print("\nEjercicio 4")
base_rectangulo = 5.5
altura_rectangulo = 3
ex04_area_rectangulo.calcular_area_rectangulo(base_rectangulo, altura_rectangulo )

print("\nEjercicio 5")
radio_circulo = 8
ex05_area_circulo.calcular_area_circulo(radio_circulo)

print("\nEjercicio 6")
numero_dividendo = 8
numero_divisor = 2
son_multiplos = ex06_multiplo.es_multiplo(numero_dividendo, numero_divisor)
if son_multiplos:
    print(f"Los numero {numero_dividendo} y {numero_divisor} son multiplos")
else:
    print(f"Los numero {numero_dividendo} y {numero_divisor} no son multiplos")

print("\nEjercicio 7")
numero = 11
es_numero_primo = ex07_validar_primo.validar_si_es_primo(numero)
if es_numero_primo:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")

print("\nEjercicio 8")
numero = 5
ex08_validar_primo_hasta.verificar_numeros_primos_hasta(numero)


print("\nEjercicio 9")
cadena = "odontologo"
caracter = "o"
cantidad_letras = ex09_contar_caracter_igual.contar_letras_coincidentes(cadena, caracter)
print(f"La cantidad de letra '{caracter}' que hay en la palabra {cadena} es {cantidad_letras}")


print("\nEjercicio 10")
cadena = "Computacion"
cantidad_caracteres = ex10_contar_caracteres.contar_caracteres(cadena)
print(f"La palabra {cadena} tiene {cantidad_caracteres} caracteres")


print("\nEjercicio 11")
ex11_palabra_maxima_longitud.palabra_mas_larga()