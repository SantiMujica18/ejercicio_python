
membresia = ["dorada", "plateada"]

valor = int(input("ingrese el valor del producto: "))

tipo = input("¿Que membresía tiene Dorada o Plateada?").lower()

consulta = tipo in membresia

descuento = valor * 0.10 
total = valor - (valor * 0.10 )

if valor > 100 or consulta:
    print(f"Tiene descuento y es {descuento} y queda en {total}")
else:
    print("No tiene membresía o su monto no supera los 100")

