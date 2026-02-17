#Buscador de Ingredientes: 
# Define una lista de ingredientes disponibles en una alacena. 
# Pide al usuario el nombre de un ingrediente y verifica, usando el operador in, si el 
# ingrediente está disponible para cocinar.

ingredients = ["chocolate", "arroz", "maiz", "cebolla","aguacate"]

escoger = input("Escoja el ingrediente: ").lower()

elegir = escoger in ingredients

if elegir:
    print(f"El ingrediente que escogio es {escoger} y esta disponible")
else:
    print("El ingrediente no esta disponible con suelte otros")
    print(ingredients)

