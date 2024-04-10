def obtener_saldo():
    while True:
        try:
            saldo = float(input("Ingrese el saldo de la cuenta: "))
            return saldo
        except ValueError:
            print("Error: Por favor ingrese un valor numérico válido.")