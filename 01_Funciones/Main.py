import Bienvenida_01
import Anio_actual_02
import Saludo_03
import Area_rectangulo_04
import Area_circulo_05
import Multiplo_06
import Validar_numero_primo_07
import Validar_primo_hasta_08
import Contar_caracter_igual_09
import Contar_caracteres_10
import Palabra_maxima_longitud

print("Ejericio 1")
Bienvenida_01.bienvenida()

print("\nEjercicio 2")
anio_actual = Anio_actual_02.obtener_año_actual()
print(f"El año actual es {anio_actual}")

print("\nEjercicio 3")
Saludo_03.saludar("Oscar")

print("\nEjercicio 4")
base_rectangulo = 5.5
altura_rectangulo = 3
Area_rectangulo_04.calcular_area_rectangulo(base_rectangulo, altura_rectangulo )

print("\nEjercicio 5")
radio_circulo = 8
Area_circulo_05.calcular_area_circulo(radio_circulo)

print("\nEjercicio 6")
numero_dividendo = 8
numero_divisor = 2
son_multiplos = Multiplo_06.es_multiplo(numero_dividendo, numero_divisor)
if son_multiplos:
    print(f"Los numero {numero_dividendo} y {numero_divisor} son multiplos")
else:
    print(f"Los numero {numero_dividendo} y {numero_divisor} no son multiplos")

print("\nEjercicio 7")
numero = 11
es_numero_primo = Validar_numero_primo_07.validar_si_es_primo(numero)
if es_numero_primo:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")

print("\nEjercicio 8")
numero = 5
Validar_primo_hasta_08.verificar_numeros_primos_hasta(numero)

print("\nEjercicio 9")
cadena = "odontologo"
caracter = "o"
cantidad_letras = Contar_caracter_igual_09.contar_letras_coincidentes(cadena, caracter)
print(f"La cantidad de letra '{caracter}' que hay en la palabra {cadena} es {cantidad_letras}")

print("\nEjercicio 10")
cadena = "Computacion"
cantidad_caracteres = Contar_caracteres_10.contar_caracteres(cadena)
print(f"La palabra {cadena} tiene {cantidad_caracteres} caracteres")

print("\nEjercicio 11")

Palabra_maxima_longitud.palabra_mas_larga()