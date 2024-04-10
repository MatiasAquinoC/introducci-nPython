def obtener_calificacion_numerica():
    while True:
        try:
            calificacion = float(input("Ingrese la calificación numérica (del 1 al 10): "))
            if calificacion < 1 or calificacion > 10:
                print("Error: La calificación debe estar en el rango del 1 al 10.")
                continue
            return calificacion
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")