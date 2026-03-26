def calcular_notas_sobre_promedio():
    # Pedimos la cantidad de notas
    n = int(input("¿Cuántas notas vas a ingresar? "))
    
    if n <= 0:
        print("La cantidad de notas debe ser mayor a cero.")
        return

    notas = []

    # Ciclo para capturar las notas uno por uno
    for i in range(n):
        nota = float(input(f"Ingresa la nota {i + 1}: "))
        notas.append(nota)

    # Calculamos el promedio
    promedio = sum(notas) / n
    print(f"\nEl promedio del curso es: {promedio:.2f}")

    # Contamos cuántas notas superan ese promedio
    contador_mayores = 0
    for nota in notas:
        if nota > promedio:
            contador_mayores += 1

    # Salida final
    print(f"La cantidad de notas mayores al promedio es: {contador_mayores}")

# Ejecutamos la función
calcular_notas_sobre_promedio()