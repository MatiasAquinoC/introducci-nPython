from asignarCalificacion import asignar_calificacion
from obtenerCalificacionNumerica import obtener_calificacion_numerica

def main():
    while True:
        print("\n1. Asignar calificación")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calificacion_numerica = obtener_calificacion_numerica()
            calificacion_literal = asignar_calificacion(calificacion_numerica)
            print("La calificación literal es:", calificacion_literal)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
