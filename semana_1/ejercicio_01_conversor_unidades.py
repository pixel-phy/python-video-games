"""Escribe un programa que:

Muestre un menú con 3 opciones de conversión.

Pida al usuario elegir una opción.

Solicite el valor a convertir (puede tener decimales).

Realice la conversión con las fórmulas dadas.

Muestre el resultado con 2 decimales.

Pregunte si quiere hacer otra conversión y repita si la respuesta es "s"."""
print("\n=== Conversor de unidades ===\n")

while True:
    # Mostrar menú cada vez
    print("\n--- Menú ---")
    print("1. km a millas")
    print("2. Celsius a Fahrenheit")
    print("3. kg a libras")
    print("s. Salir")
    
    entrada = input("Elija una opción: ")
    
    if entrada.lower() == 's':
        print("¡Hasta luego!")
        break
    
    # Validar que sea número
    try:
        opcion = int(entrada)
    except ValueError:
        print("❌ Error: Debes ingresar un número (1, 2, 3) o 's' para salir.")
        continue  # Vuelve a mostrar el menú
    
    # Validar que esté entre 1 y 3
    if opcion not in [1, 2, 3]:
        print("❌ Error: Opción no válida. Elige 1, 2 o 3.")
        continue  # Vuelve a mostrar el menú
    
    # Opción 1: km a millas
    if opcion == 1:
        try:
            valor_km = float(input("Ingrese los kilómetros: "))
            millas = valor_km * 0.621371
            print(f"{valor_km} km son {millas:.2f} millas.")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
    
    # Opción 2: Celsius a Fahrenheit
    elif opcion == 2:
        try:
            valor_celsius = float(input("Ingrese los grados Celsius: "))
            fahrenheit = (valor_celsius * 9/5) + 32
            print(f"{valor_celsius} °C son {fahrenheit:.2f} °F")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
    
    # Opción 3: kg a libras
    elif opcion == 3:
        try:
            valor_kg = float(input("Ingrese los kilogramos: "))
            libras = valor_kg * 2.20462
            print(f"{valor_kg} kg son {libras:.2f} libras")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")