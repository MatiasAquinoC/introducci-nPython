import math
from gradosARadianes import grados_a_radianes
from radianesASexagesimales import radianes_a_grados

def main():
    while True:
        print("1. Convertir de grados sexagesimales a radianes")
        print("2. Convertir de radianes a grados sexagesimales")
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == "1":
            grados = float(input("Ingrese la cantidad de grados: "))
            if grados < 0:
                print("Error: No se pueden ingresar valores negativos.")
            else:
                radianes = grados_a_radianes(grados)
                print(f"{grados} grados son equivalentes a {radianes:.2f} radianes.")
        elif opcion == "2":
            radianes = float(input("Ingrese la cantidad de radianes: "))
            if radianes < 0:
                print("Error: No se pueden ingresar valores negativos.")
            else:
                grados = radianes_a_grados(radianes)
                print(f"{radianes:.2f} radianes son equivalentes a {grados} grados.")
        else:
            print("Opción no válida. Por favor seleccione 1 o 2.")
            continue
        
        seguir = input("¿Desea realizar otra conversión? (s/n): ")
        if seguir.lower() != 's':
            break

if __name__ == "__main__":
    main()