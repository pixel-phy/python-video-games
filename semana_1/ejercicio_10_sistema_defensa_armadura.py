"""Sistema de defensa y armadura (con Raise)
Escribe un programa que:
1. Pregunte el daño que haría el enemigo (número decimal, debe ser mayor a 0).
2. Pregunte la armadura del jugador (número entero entre 0 y 20).
3. Pregunte si el jugador está en posición de defensa (s o n).

Calcule el daño final con estas reglas:
4. Reducción por armadura: cada punto de armadura reduce 5% del daño.
5. La armadura no puede reducir más del 80% del daño total.
6. Si está en defensa, reduce 50% adicional.

Use raise para validar:
7. Si el daño es menor o igual a 0 → raise ValueError("El daño debe ser mayor a 0")
8. Si la armadura está fuera del rango 0-20 → raise ValueError("La armadura debe estar entre 0 y 20")
9. Capture los errores con try/except y muestre mensajes amigables.
10. Repita hasta que el usuario escriba "salir"."""

print("\n=== SISTEMA DE DEFENSA Y ARMADURA ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Daño del enemigo
    entrada1 = input("Daño del enemigo: ").strip()
    if entrada1.lower() == 'salir':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

    try:
        daño_enemigo = float(entrada1)
        if daño_enemigo <= 0:
            raise ValueError("El daño debe ser mayor que 0.")
    except ValueError as e:
        print(f"Error: {e}\n")
        continue

    # Armadura del jugador
    entrada2 = input("Armadura del jugador entre (0 - 20): ").strip()
    if entrada2.lower() == 'salir':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    try:
        armadura = int(entrada2)
        if armadura < 0 or armadura > 20:
            raise ValueError("La armadura debe estar entre 0 y 20.")
    except ValueError as e:
        print(f"Error: {e}")
        continue
    
    # Posición de defensa
    entrada3 = input("¿Posición de defensa? (s/n): ").strip()
    if entrada3.lower() == 'salir':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

    defensa = entrada3.lower() == 's'

    # Calculos
    # Reducción por armadura
    reduccion_armadura_porcentaje = armadura * 0.05
    if reduccion_armadura_porcentaje > 0.8:
        reduccion_armadura_porcentaje = 0.8
        print("La armadura supera el 80% de reducción máxima. Se aplica 80%")

    daño_con_armadura = daño_enemigo * (1- reduccion_armadura_porcentaje)
    valor_reducido_armadura = daño_enemigo - daño_con_armadura

    # Reducción por defensa si aplica
    if defensa:
        daño_final = daño_con_armadura * 0.5
        valor_reducido_defensa = daño_con_armadura - daño_final
    else:
        daño_final = daño_con_armadura
        valor_reducido_defensa = 0

    # Mostramos resultados
    print("\n--- Resultados ---")
    print(f"Daño original: {daño_enemigo:.2f}")
    print(f"Reducción con armadura ({armadura} --> {reduccion_armadura_porcentaje*100:.0f}%): {valor_reducido_armadura:.2f}")

    if defensa:
        print(f"Reducción por defensa: -{valor_reducido_defensa:.2f}")
    
    print(f"Daño final recibido: {daño_final:.2f}")

    # Preguntar si quiere volver a jugar
    repetir = input("\n¿Calcular otra vez? (s/n): ")
    if repetir != 's':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

    print()

