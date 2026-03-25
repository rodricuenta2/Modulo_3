#4. Ciclo infinito controlado con break
#Escribe un ciclo while True que solicite ingresar un número. El ciclo debe terminar si el número ingresado es
#0. Usa break para salir.


while True:
    numero = int(input("Ingresa un número: ")) # solicita ingresar el numero
    
    if numero == 0: # si el numero ingresado es 0 se termina el programa
        print("Programa terminado!")
        break
        
   