#6. Uso de continue
#Recorre una lista de nombres. Si el nombre es "Juan", omítelo usando continue. Imprime todos los demás.
#Recuerda aplicar snake_case para las variables y comentar cada ejercicio explicando qué hace el
#ciclo y qué controla su finalización.

nombres =["roberto","miguel","juan","pedro","carlos"] # se define la lista de nombres

for nombre in nombres: # para cada indice dentro de la lista
    if nombre == "juan": # si el indice es igual a juan
        continue # se saltara a la siguiente instruccion que es imprimir el resto de nombres que no son igual a juan
    
    print(nombre) 