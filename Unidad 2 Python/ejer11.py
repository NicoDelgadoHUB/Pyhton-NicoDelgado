def concesionario():
    autos_vendidos = int(input("Ingrese el numero de autos vendidos:"))
    valor_auto = int(input("Ingrese el valor del auto:"))
    salario_base = 5500 + (autos_vendidos * 200)
    adicional = valor_auto * 0.05

    salario_total = salario_base + adicional

    print("El salario total del vendedor es:", salario_total)

concesionario()    