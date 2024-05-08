def porcentaje():
# Solicitar al usuario que ingrese la cantidad parcial y la cantidad total
    cantidad_parcial = int(input("Ingrese la cantidad parcial: "))
    cantidad_total = int(input("Ingrese la cantidad total: "))

# Calcular el porcentaje
    porcentaje = (cantidad_parcial / cantidad_total) * 100

    print("El porcentaje que representa la primera de la segunda", porcentaje)
porcentaje()    