def obtener_lado_cuadrado():
    while True:
        try:
            lado = int(input("Ingrese el número de asteriscos por lado del cuadrado: "))
            if lado <= 0:
                print("Error: El número debe ser positivo y mayor que cero.")
                continue  
            return lado
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            continue 