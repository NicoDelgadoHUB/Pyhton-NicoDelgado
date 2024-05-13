def nota_final():
    parciales = int(input("Ingrese la nota del examen parcial del 1 al 10: ")) 
    practicos = int(input("Ingrese la nota de los tp del 1 al 10: ")) 
    integrador = int(input("Ingrese la nota del examen integrador del 1 al 10: ")) 

    examenes_parciales = parciales * 0.3
    trabajos_practicos =  practicos * 0.2
    examen_integrador = integrador * 0.5

    nota_final = examenes_parciales + trabajos_practicos + examen_integrador
    print("La nota final es:", nota_final)
     
nota_final()    