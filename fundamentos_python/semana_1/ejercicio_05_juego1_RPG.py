"""Escribe un programa para un juego RPG que:
1. Pregunte el daño base de un arma (número entero o decimal).
2. Pregunte un multiplicador de crítico (ej: 1.5 = 150% de daño).
3. Pregunte si el ataque es crítico (el usuario escribe "s" o "n").

Calcule el daño total:
4. Si es crítico: daño_total = daño_base * multiplicador
5. Si no es crítico: daño_total = daño_base
6. Muestre el daño total redondeado a 2 decimales.
7. Repita hasta que el usuario escriba "salir". """

print("\n=== JUEGO RPG ===\n")
print("\nEscriba 'salir' para terminar.")

while True:
    # Entrada del daño base del arma
    entrada = input("Ingresa el daño base del arma (int/float): ").strip()
    if entrada.lower() == 'salir':
        print("Adiós!")
        break
    try:
        daño_base = float(entrada)
    except ValueError:
        print("Ingrese un valor numérico por favor.")
        continue

    # Multiplicador de critico
    entrada_2 = input("Ingresa el multiplicador de critico (Ej: 1.5 = 150 %. Daño adicional.): ").strip()
    if entrada_2.lower() == 'salir':
        print("Adiós!")
        break
    try:
        multiplicador = float(entrada_2)
    except ValueError:
        print("Ingrese un valor numérico válido.")
        continue

    # Es critico o no
    entrada_3 = input("El ataque es crítico ('s' o 'n'): ").strip()
    if entrada_3.lower() == 'salir':
        print("Adiós!")
        break
    
    # Calculamos daños
    if entrada_3.lower() == 's':
        daño_total = daño_base * multiplicador
    else:
        daño_total = daño_base

    # Mostramos datos
    print(f"El daño total es: {daño_total:.2f}")

    # Preguntar si desea seguir atacando
    repetir = input("¿Quieres hacer otro ataque? (s/n): ").lower()
    if repetir != 's':
        print("Buena partida!")
        break

    print()