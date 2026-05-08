"""Escribe un programa para un juego RPG que simule el uso de una poción de curación.
El programa debe:
1. Preguntar la vida actual del jugador.
2. Preguntar la vida máxima del jugador.
3. Preguntar cuántos puntos de vida cura la poción (puede ser un número fijo o un porcentaje).
4. Preguntar si la curación es por puntos fijos o por porcentaje (p para puntos, % para porcentaje).
5. Calcular la vida después de usar la poción:

Si es por puntos: vida_nueva = vida_actual + curacion

Si es por porcentaje: vida_nueva = vida_actual + (vida_maxima * curacion / 100)

6. Validar que la vida nueva no supere la vida máxima.
7. Mostrar la vida después de la curación.

8. Repetir hasta que el usuario escriba "salir".
"""

print("\n=== SISTEMA DE CURACIÓN RPG ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Vida actual
    entrada1 = input("Vida actual del personaje: ").strip()
    if entrada1.lower() == 'salir':
        print("¡Buena partida!")
        break
    try:
        vida_actual = float(entrada1)
        if vida_actual < 0:
            print("❌ La vida no puede ser negativa. Se usará 0.")
            vida_actual = 0
    except ValueError:
        print("❌ Ingresa un valor numérico válido.\n")
        continue

    # Vida máxima
    entrada2 = input("Vida máxima del personaje: ").strip()
    if entrada2.lower() == 'salir':
        print("¡Buena partida!")
        break
    try:
        vida_maxima = float(entrada2)  # ← Corregido: float
        if vida_maxima <= 0:
            print("❌ La vida máxima debe ser mayor a 0.\n")
            continue
        if vida_actual > vida_maxima:
            print("⚠️ La vida actual no puede superar la máxima. Se ajustará.")
            vida_actual = vida_maxima
    except ValueError:
        print("❌ Ingresa un valor numérico válido.\n")
        continue

    # Tipo de curación
    entrada4 = input("¿Curación por puntos (p) o porcentaje (%)?: ").strip()
    if entrada4.lower() == 'salir':
        print("¡Buena partida!")
        break

    # Valor de curación
    entrada3 = input("¿Cuánto cura la poción?: ").strip()
    if entrada3.lower() == 'salir':
        print("¡Buena partida!")
        break
    try:
        valor_curacion = float(entrada3)  # ← Corregido: float
        if valor_curacion < 0:
            print("❌ La curación no puede ser negativa.\n")
            continue
    except ValueError:
        print("❌ Ingresa un valor numérico válido.\n")
        continue

    # Calcular vida nueva
    if entrada4.lower() == 'p':
        vida_nueva = vida_actual + valor_curacion
    elif entrada4.lower() == '%':
        vida_nueva = vida_actual + (vida_maxima * valor_curacion / 100)
    else:
        print("❌ Opción no válida. Usa 'p' o '%'.\n")
        continue

    # Validar límite de vida máxima
    if vida_nueva > vida_maxima:
        curacion_real = vida_maxima - vida_actual
        print(f"⚠️ Solo necesitabas {curacion_real:.1f} puntos para llegar al máximo.")
        vida_nueva = vida_maxima

    # Mostrar resultado
    print(f"\n❤️ Vida: {vida_actual:.1f} → {vida_nueva:.1f} / {vida_maxima:.1f}")

    # Preguntar si repetir
    entrada5 = input("\n¿Usar otra poción? (s/n): ").strip()
    if entrada5.lower() != 's':
        print("\n¡Hasta luego, guerrero! 🏆")
        break

    print()