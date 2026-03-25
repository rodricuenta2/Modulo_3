# 3. Condición en un ciclo
#Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime "Par", si es impar,
#imprime "Impar".

# creamos la lista a recorrer
numeros =[1,2,3,4,5,6,7,8,9,10]


for i in numeros:

# ponemos la condicion que nos indicara si el numero ingresado es par o impar.
    if i % 2 == 0:
      print(f"{i}  Par") # la letra f inserta el valor de la variable en el texto
    else:
        print(f"{i} Impar")