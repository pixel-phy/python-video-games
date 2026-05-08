print("\n=== Analizador de números ===\n")
print("(Para salir, escribe 'salir')\n")

while True:  # Bucle infinito, se rompe con 'break'
    entrada = input("Ingrese un número entero (o 'salir'): ")
    
    if entrada.lower() == 'salir':  # Normalizamos a minúsculas
        print("¡Hasta luego!")
        break  # Sale del bucle
    
    try:
        numero = int(entrada)  # Intentamos convertir a entero
    except ValueError:
        print("❌ Error: Debes ingresar un número entero o la palabra 'salir'.\n")
        continue  # Vuelve a pedir
    
    # --- Cálculos comunes ---
    valor_absoluto = abs(numero)
    multiplicacion = numero * 3
    
    # --- Determinar positivo/negativo/cero ---
    if numero > 0:
        signo = "positivo"
    elif numero < 0:
        signo = "negativo"
    else:
        signo = "cero"
    
    # --- Determinar par/impar (solo si no es cero) ---
    if numero == 0:
        par_impar = "no es par ni impar"
    elif numero % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "impar"
    
    # --- Mostrar resultado final ---
    print(f"El número {numero} es {signo}, {par_impar}, "
          f"su valor absoluto es {valor_absoluto} "
          f"y multiplicado por 3 da {multiplicacion}.\n")