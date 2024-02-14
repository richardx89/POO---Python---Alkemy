#Sumar o restar dos números dados por el usuario, según la opción elegida por el mismo
def suma(a, b):
    # Función para la suma
    resultado = a + b
    print("Resultado de la suma:", resultado)

def resta(a, b):
    # Función para la resta
    resultado = a - b
    print("Resultado de la resta:", resultado)

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Para realizar la suma de dos números marque 1")
        print("2. Para realizar la resta de dos números marque 2")
        print("3. Salir")

        opcion = input("Ingresa el número de la opción: ")

        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            suma(a,b)
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            resta(a,b)
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

if __name__ == "__main__":
    main()