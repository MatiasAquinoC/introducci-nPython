from calcularRaizCuadrada import calcular_raiz_cuadrada
from numeroPositivo import obtener_numero_positivo

def main():
    while True:
        print("1. Calcular la raíz cuadrada de un número")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = obtener_numero_positivo()
            raiz_cuadrada = calcular_raiz_cuadrada(numero)
            print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
            
            seguir = input("¿Desea calcular la raíz cuadrada de otro número? (s/n): ")
            if seguir.lower() != 's':
                break
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()