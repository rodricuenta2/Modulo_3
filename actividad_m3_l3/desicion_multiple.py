
# Solicita al usuario una calificación (entre 1 y 7) e imprime el resultado evaluativo:
# • 7 → Excelente
# • 6 → Muy bien
# • 5 → Bien
# 4 → Suficiente
# • Menor que 4 → Insuficiente

nota = int(input("Ingrese una nota entre 1 y 7 : "))

if nota == 7:
    print("Excelente")
    
elif nota == 6:
    print("Muy Bien")
    
elif nota == 5:
    print("Bien")

elif nota == 4:
    print("Suficiente")
    
else:
    nota < 4
    print("Insuficiente")

    