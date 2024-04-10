def asignar_calificacion(calificacion):
    if calificacion >= 9.1 and calificacion <= 10:
        return "A Excelente"
    elif calificacion >= 8.1 and calificacion < 9.1:
        return "B Muy bien"
    elif calificacion >= 7.5 and calificacion < 8.1:
        return "C Bien"
    else:
        return "R Reprobado"