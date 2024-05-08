def segundos():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))

    total_segundos = horas * 3600 + minutos * 60 + segundos
    print("El total de segundos es:", total_segundos)

segundos()