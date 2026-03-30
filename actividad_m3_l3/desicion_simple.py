# Solicita al usuario ingresar un número. Si es mayor o igual a 18, imprime "Eres mayor de edad". Si no,
# imprime "Eres menor de edad".


edad = 18
numero = int (input("ingresa un numero : " ))

if numero >= edad:
    print("Eres mayor de edad")
elif numero <= edad:
    print("Eres menor de edad")
   