from calcularInteres import calcular_interes
from obtenerSaldo import obtener_saldo

def main():
    while True:
        try:
            saldo = obtener_saldo()
            interes = calcular_interes(saldo)
            saldo_final = saldo + interes
            print(f"El saldo final después de un año es: {saldo_final:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

        seguir = input("¿Desea realizar otra operación? (s/n): ")
        if seguir.lower() != 's':
            break

if __name__ == "__main__":
    main()
