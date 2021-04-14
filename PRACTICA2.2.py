#INGRESAREMOS LA FECHA EN EL FOMATO INDICADO EN LA PRACTICA Y UTILIZREMOS UNA FUNCION ".lower()" que sirve para convertir cualquier cosa ingresada en el input en minuscula
ingresa = input("Ingresa la fecha en el formato 'dia, DD/MM'").lower()
#luego separararemos los datos ingresados, en este caso dividiremos con split lo que hemos puesto en ingresa, y especificaremos que estos datos estan divididos por una coma
dia_semana, fecha = ingresa.split(",")
#ahora dividiremos la fecha pero especificaremos que esta vez estan divididos por una barra /
dia, mes = fecha.split("/")
#LO QUE HAREMOS A CONTINUACION SERA COMPROBAR QUE HAYA ESCRITO UNA FECHA CORRECTA
if int(dia) <= 31 and int(mes) <= 12:
#SI todo SALIO CORRECTO VERIFICARA QUE DIA DE LA SEMANA SE ELIGIO, PRIMERO COMENZARA POR LOS LUNES, MIERCOLES Y VIERNES 
    if dia_semana in "lunes, martes, miercoles":
        #SI ELEGIMOS UNO DE ESOS DIAS PREGUNTARA SI HUBO EXMAEN
        exam = input("¿Hay examen?").lower()
        #EN CASO DE HABER PRESENTADO EXAMEN SE PREGUNTARA CUANTOS ALUMNOS REPROBARON, CUANTOS APROBARON
        if exam == "si":
            alum_repro = int(input("Cuantos alumnos reprobaron?"))
            alum_apro = int(input("Cuantos alumnos aprobaron? "))
            #LUEGO SE SACARA UN PORCENTAJE DE LOS ALUMNOS APROBADOS
            porcentaje = (alum_apro/(alum_apro+alum_repro))*100
            print(f"El porcentaje de aprobados es:  {porcentaje} %")
            #en caso de no haber examen se motrara en la pantalla
        elif exam == "no":
            print("No hay examen")
    #en caso de haber seleccionado un jueves        
    elif dia_semana == "jueves":
    #se preguntara el porcentaje de asistencia
        porcentaje = int((input("Cual fue el procentaje de asistencia")))
        #si el porcentaje fue mayor de 50 se mostarra un mensaje
        if porcentaje > 50:
            print("Fue la mayoria")
        #en caso de nos er asi, se mostrara otro
        else:
            print("No fue la mayoria")
    #Si fuera viernes y ademas fuera inicio de año
    elif dia_semana == "viernes" and int(dia) == 1 and int(mes) == 1:
        #se mostrara el siguiente mensaje
        print("Bienvenido al nuevo semestre")
        #luego se preguntara la canridad de alumnos que entraron de nuevo ingreso
        alumnos = int(input("Cuantos alumnos van a ingresa? "))
        #El costo de la inscripcion
        inscripcion = int(input("Cuanto cobran de inscripcion? "))
        #Y se calucla el total de los ingresos por la inscripcion, luego se imprime el resultado
        ingreso_total = (alumnos*inscripcion)
        print("El ingreso total del semestre es de {ingreso_total} pesos")
    #Si fuera fin de semana se muestra un mensaje
    elif dia_semana == "sabado" or dia_semana == "domingo":
        print("Este dia no hay clases")
    #En caso de ingresar un dia no valido se muestra el siguiente mensaje
    else:
        print("iNTENTALO DE NUEVO")
#En caso de ingresar una fecha no valido se muestra el siguiente mensaje
else:
    print("Intentelo de nuevo")
            

