#1. Crear estructuras
#Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:
#• Lista (list)
#• Tupla (tuple)
#• Conjunto (set)
#• Diccionario (dict)
#Muestra cada estructura usando print() y comenta brevemente su diferencia principal.

# esto corresponde a una lista, es modificable.
numeros = [1,2,3,4,5,6,7,8]
print(numeros)

# esto corresponde a una tupla, los datos van entre estos parentesis() y su contenido no se puede modificar.
nombres = ("rodrigo","matias","juan","pablo","miguel") 
print(nombres)

# esto es un conjunto, va entre estos parentesis {} y se carateriza ademas porque no permite tener elementos duplicados y no tener un orden fijo.
frutas = {"manzana", "banana", "cereza", "naranja","uva"}
print(frutas)

# esto corresponde a diccionario, funciona en formato clave y valor, van dentro de este parentesis {}, sus datos son modificables.
informacion =  {
  "Nombre": "Rodrigo",
  "Edad": 47,
  "Ciudad": "Valdivia",
  "Telefono": 981501209,
  "Documento": 96990243,
  "Profesion": "Ingeniero"
}
print(informacion)

#Contar e iterar

#Usa len() para mostrar la cantidad de elementos en cada estructura.

print(len(numeros)) # esto muestra la cantidad de elementos de la lista
print(len(nombres)) # esto muestra la cantidad de elementos de la tupla
print(len(frutas))  # esto muestra la cantidad de elementos del conjunto
print(len(informacion)) # esto muestra la cantidad de elementos del diccionario



#Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.

for numero in numeros:
    print(numero)

for nombre in nombres:
    print(nombre)

for fruta in frutas:
    print(fruta)
    
for info in informacion:
    print(info)


#Modificar estructuras

#Agrega un nuevo elemento a la lista y al conjunto.

numeros.append(9) # se agrega elemento a la lista con metodo append
print(numeros)

frutas.add("pera") # se agrega elemento al conjunto con metodo add
print(fruta)

#Borra un elemento de la lista.

numeros.remove(5) # se borra un elemento de la lista con metodo remove, borrara el elemento de valor 5
print(numeros) # al hacer print el numero 5 ya no esta en la lista


#Agrega una nueva clave al diccionario.

informacion["mail"] = "rodrigo.estroz@gmail.com" # esto agrega una clave al dicconario
print(informacion)

#Intenta modificar la tupla y comenta qué ocurre.

#NO ES POSBLE DATOS MODIFICAR DATOS DE UNA TUPLA, SU PRINCIPAL CARACTERISTICA ES QUE ES INMUTABLE,POR LO QUE NO HABRIA UN METODO PARA ESO, LA ALTERNATIVA SERIA CONVERTIR A LISTA, HACER LA MODIFICACION Y VOLVER A DEJAR COMO TUPLA.
