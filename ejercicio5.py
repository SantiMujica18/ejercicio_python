#Clasificación de Números Anidados: Solicita un número entero al usuario. 
# Primero, verifica si el número es positivo, negativo o cero. Si es positivo, 
# añade un segundo nivel de decisión (anidamiento) para determinar si es un número par o impar.

numero = int(input("Ingrese un numero entero: "))

if numero > 0:
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("Es impar")
elif numero == 0:
    print("el numero es 0")
    
else:
    print("El numero es negativo")