
def obtener_numero_positivo():
    while True:
        try:
            numero = float(input("Ingrese un número positivo: "))
            if numero < 0:
                print("Error: El número debe ser positivo.")
            else:
                return numero
        except ValueError:
            print("Error: Ingrese un número válido.")