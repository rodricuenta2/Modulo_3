# Solicita un número entero.
# • Si es positivo, imprime "Número positivo".
# • Si es cero, imprime "Es cero".
# • Si es negativo, imprime "Número negativo".
# Este ejercicio debe usar condiciones anidadas (if dentro de otro if).


entero = int(input ("Ingresa un numero entero : "))

if entero > 0:
    print("Numero Positivo")
else:
    if entero < 0:
     print("Numero Negativo")
    else:
        if entero ==0:
            print("Es cero")
                  
                    