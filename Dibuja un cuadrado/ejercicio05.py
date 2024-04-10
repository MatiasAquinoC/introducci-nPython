from crearCuadrado import crear_cuadrado
from obtenerLado import obtener_lado_cuadrado

def main():
    while True:
        print("\n1. Crear cuadrado de asteriscos")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lado = obtener_lado_cuadrado()
            crear_cuadrado(lado)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
