
edad = int(input("Ingrese su edad: "))

invitacion = ["s"]

consulta = input("¿tiene una invitacion? S/N: ").lower()

valido = consulta in invitacion

if edad >= 18 and valido:
    print("pasa")
else:
    print("no pasa")





