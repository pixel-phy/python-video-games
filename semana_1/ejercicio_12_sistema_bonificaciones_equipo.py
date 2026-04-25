""" Escribe un programa para un juego RPG que calcule la bonificación de estadísticas según la afinidad elemental del personaje.
1. Preguntar el nombre del personaje.
2. Preguntar su estadística base (fuerza, entre 1 y 100).
3. Preguntar su afinidad elemental entre:
- fuego → bonificación +25%
- hielo → bonificación +20%
- rayo → bonificación +30%
- tierra → bonificación +15%
- ninguna → sin bonificación
4. Preguntar si tiene objeto legendario (s o n), que suma +10 adicional.
5. Calcular la estadística final:
con_bonificacion = estadistica_base * (1 + porcentaje/100)
estadistica_final = con_bonificacion + (10 si tiene objeto legendario else 0)
6. Validar que la estadística no supere 150 (máximo permitido).
7. Mostrar el resultado detallado.
8. Repetir hasta que el usuario escriba "salir"."""

print("\n--- SISTEMA DE BONIFICACIONES ---\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Pregunto por el nombre
    nombre_personaje = input("Nombre del personaje: ").strip()
    if nombre_personaje.lower() == 'salir':
        print("¡Hasta la próxima!")
        break

    # Estadística base
    entrada2 = input("Estadística base (1-100): ").strip()
    if entrada2.lower() == 'salir':
        print("¡Hasta la próxima!")
        break
    
    try:
        estadistica_base = float(entrada2)
        if estadistica_base < 1 or estadistica_base > 100:
            raise ValueError("La estadística debe estar entre 1 y 100")
    except ValueError as e:
        print(f" Error: {e}\n")
        continue

    # Afinidad elemental
    entrada3 = input("Afinidad elemental (fuego/hielo/rayo/tierra/ninguna): ").strip()
    if entrada3.lower() == 'salir':
        print("¡Hasta luego!")
        break

    afinidad = entrada3.lower()
    
    if afinidad == 'fuego':
        bonificacion = 0.25
    elif afinidad == 'hielo':
        bonificacion = 0.20
    elif afinidad == 'rayo':
        bonificacion = 0.30
    elif afinidad == 'tierra':
        bonificacion = 0.15
    elif afinidad == 'ninguna':
        bonificacion = 0
    else:
        print("❌ Afinidad no reconocida. Usa: fuego/hielo/rayo/tierra/ninguna\n")
        bonificacion = 0
        continue

    # Objeto legendario
    entrada4 = input("¿Tiene objeto legendario? (s/n): ").strip().lower()
    if entrada4 == 'salir':
        print("¡Hasta luego!")
        break
    
    if entrada4 == 's':
        objeto_legendario = 10
    else:
        objeto_legendario = 0

    # Calculo
    estadistica_total = estadistica_base + objeto_legendario + (estadistica_base * bonificacion)

    # Validación del límite máximo permitido
    if estadistica_total > 150:
        print("La estadística superó los 150 puntos. Se ajusta al máximo.")
        estadistica_total = 150

    # Mostramos resultados
    print("\n--- RESULTADO ---")
    print(f"{nombre_personaje}")
    print(f"Estadística base: {estadistica_base:.0f}")
    print(f"Bonificación por afinidad ({afinidad} → +{bonificacion*100:.0f}%): +{estadistica_base * bonificacion:.0f}")
    print(f"Bonificación por objeto legendario: +{objeto_legendario}")
    print(f"Estadística final: {estadistica_total:.0f}")

    # --- REPETIR ---
    repetir = input("\n¿Calcular otra estadística? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Hasta luego!")
        break
    
    print()