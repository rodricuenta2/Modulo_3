

cantidad = int(input("¿ Cuántas notas se van a ingresar ? : ")) # se pregunta cuantas notas se ingresaran/ se transforma a entero


notas = [] # aqui creamos la variable "notas" que es una lista vacia donde se guardaran las notas

# SE PIDEN NOTAS UNA POR UNA
for a in range(cantidad): # para indice dentro de un "rango" que estara dado por lo que se ingresa
    nota = float(input(f"Ingrese nota {a+1}: ")) # se define variable nota como lo que usuario ingresara/ se transforma a decimal(float)
    notas.append(nota) # en lista notas se ira agregando "nota" que es lo que igresa el usuario


promedio = sum(notas) / cantidad # calculo de promedio que corresponde a la suma de todas las notas dividido por la cantidad de estas

# CONTAR NOTAS QUE SON MAYORES AL PROMEDIO
mayor = 0 # variable mayor comienza en 0
for n in notas:  # para n(indice) en la lista notas
    if n > promedio: # preguntamos si indice es mayor al promedio
        mayor = mayor + 1 # entonces a variable mayor se le ira sumando 1 (mayor = 0 + 1)

# SE MUESTRA LOS RESULTADOS
print(f"El promedio es: {promedio}") # aqui mostramos el promedio 
print(f"La cantidad de notas mayores al promedio es: {mayor}") # aqui se muestran las notas mayores al promedio