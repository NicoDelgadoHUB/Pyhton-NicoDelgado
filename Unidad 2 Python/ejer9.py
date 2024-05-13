def fecha_num():
    fecha_numerica = int(input("Ingrese una fecha en formato DDMMAAAA: "))

    dia = fecha_numerica // 1000000  # Dividir por un millón para obtener los dos primeros dígitos (día)
    mes_anio_temp = fecha_numerica % 1000000  # Obtener los seis últimos dígitos (mes y año)
    mes = mes_anio_temp // 10000  # Dividir por diez mil para obtener los dos dígitos del mes
    anio = mes_anio_temp % 10000  # Los últimos cuatro dígitos son el año

    # Imprimir los resultados
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)

fecha_num()    