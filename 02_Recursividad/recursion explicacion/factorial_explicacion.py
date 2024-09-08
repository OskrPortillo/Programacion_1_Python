'''

# llamada 1°
def factorial(numero: int):                     # numero =  5
    if numero == 0 or numero == 1:              # Esta condicion es falsa
        return 1
    else:
        anterior = numero - 1                   # anterior = 4
        return numero * factorial(anterior)     # 5 * factorial(4) , esta instruccion queda pendiente porque vuelve a llamarse a si misma
                                                # pero con un numero distinto

# llamada 2°
def factorial(numero: int):                     # numero =  4
    if numero == 0 or numero == 1:              # Esta condicion es falsa
        return 1
    else:
        anterior = numero - 1                   # anterior = 3
        return numero * factorial(anterior)     # 4 * factorial(3) , esta instruccion queda pendiente porque vuelve a llamarse a si misma
                                                # pero con un numero distinto
    
# llamada 3°
def factorial(numero: int):                     # numero =  3
    if numero == 0 or numero == 1:              # Esta condicion es falsa
        return 1
    else:
        anterior = numero - 1                   # anterior = 2
        return numero * factorial(anterior)     # 3 * factorial(2) , esta instruccion queda pendiente porque vuelve a llamarse a si misma
                                                # pero con un numero distinto
    
# llamada 4°
def factorial(numero: int):                     # numero =  2
    if numero == 0 or numero == 1:              # Esta condicion es falsa
        return 1
    else:
        anterior = numero - 1                   # anterior = 1
        return numero * factorial(anterior)     # 2 * factorial(1) , esta instruccion queda pendiente porque vuelve a llamarse a si misma
                                                # pero con un numero distinto
    
# llamada 5°
def factorial(numero: int):                     # numero =  1
    if numero == 0 or numero == 1:              # Esta condicion es verdadera, el caso base detiene la recursion y empieza a ejecutarse lo pendiente
        return 1                                # retorna 1, a la funcion de la 4° llamada         
    else:
        anterior = numero - 1                   
        return numero * factorial(anterior)

     
# llamada 4° - que estaba pendiente
def factorial(numero: int):                     
    if numero == 0 or numero == 1:              
        return 1
    else:
        anterior = numero - 1                   
        return numero * factorial(anterior)     # 2 * factorial(1)
                                                # Ahora sabemos el valor de factorial(1) = 1
                                                # calcula 2 * 1
                                                # retorna 2, a la funcion de la 3° llamada  

# llamada 3° - que estaba pendiente
def factorial(numero: int):                     
    if numero == 0 or numero == 1:              
        return 1
    else:
        anterior = numero - 1                   
        return numero * factorial(anterior)     # 3 * factorial(2) 
                                                # Ahora sabemos el valor de factorial(2) = 2   
                                                # calcula 3 * 2
                                                # retorna 6, a la funcion de la 2° llamada  

# llamada 2° - que estaba pendiente
def factorial(numero: int):                     
    if numero == 0 or numero == 1:              
        return 1
    else:
        anterior = numero - 1                   
        return numero * factorial(anterior)     # 4 * factorial(3) 
                                                # Ahora sabemos el valor de factorial(3) = 6   
                                                # calcula 4 * 6
                                                # retorna 24, a la funcion de la 1° llamada  

# llamada 1° - que estaba pendiente
def factorial(numero: int):                     
    if numero == 0 or numero == 1:              
        return 1
    else:
        anterior = numero - 1                   
        return numero * factorial(anterior)     # 5 * factorial(4) 
                                                # Ahora sabemos el valor de factorial(4) = 24   
                                                # calcula 5 * 24
                                                # retorna 120 

'''

def factorial(numero: int):
    if numero == 0 or numero == 1:
        return 1
    else:
        anterior = numero - 1
        return numero * factorial(anterior)
    

print(factorial(5))
