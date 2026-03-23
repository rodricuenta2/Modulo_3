#. Ciclo anidado
#Escribe un programa que imprima una tabla de multiplicar del 1 al 3, usando un ciclo for dentro de otro for.

# Programa para imprimir las tablas del 1 al 3


for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("---")