
# Solicita al usuario un número entre 1 y 100.
# • Si el número es exactamente 1 o 100, imprime "Estás en un límite permitido".
# • Si está dentro del rango pero no es extremo, imprime "Dentro del rango".
# • En cualquier otro caso, imprime "Fuera del rango".
# Asegúrate de usar nombres de variables en estilo snake_case y comentar el propósito de cada
# bloque de código.



# se define variable rango como el valor que ingresara usuario entre 1 y 100
numero_rango = int(input("Ingresa un numero entre 1 y 100 : "))

# se compara si lo que ingresa es = a 1 y 100
if numero_rango == 1 or numero_rango == 100:
    
    # si se cumple imprime mensaje
    print("Estas en un limite permitido")
    
    # se compara si lo que ingresa en menor a 100 y mayor que 1
elif numero_rango > 1 or numero_rango < 100:
    
    # si se cumple imprime mensaje
    print("Dentro del rango")
    
    # si no se cumple ninguna de las anteriores
else:
    print("Fuera de rango")

    
    