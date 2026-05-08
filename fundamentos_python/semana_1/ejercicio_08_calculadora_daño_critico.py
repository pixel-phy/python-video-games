"""El programa debe:
1. Preguntar el daño base del arma.
2. Preguntar la fuerza del jugador (cada punto de fuerza suma +5% al daño base).
3. Preguntar el multiplicador de crítico (si el ataque es crítico o no).
4. Preguntar si el ataque tiene bonificación elemental (fuego, hielo, rayo), que suma un 20% extra.

5. Calcular el daño final con esta fórmula:

daño_bruto = daño_base + (daño_base * fuerza * 0.05)
daño_critico = daño_bruto * multiplicador
daño_final = daño_critico * (1 + bonificacion_elemental/100)

Donde:

multiplicador = 2.0 si es crítico, 1.0 si no.
bonificacion_elemental = 20 si es fuego/hielo/rayo, 0 si no
Mostrar el daño final redondeado a 2 decimales y un resumen del cálculo.

Repetir hasta que el usuario escriba "salir". """
print("\n=== CALCULADORA DE DAÑO CRÍTICO ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Daño base del arma
    entrada1 = input("Daño base del arma: ").strip()
    if entrada1.lower() == 'salir':
        print("¡Hasta luego, guerrero!")
        break
    try:
        daño_base = float(entrada1)
        if daño_base < 0:
            print("⚠️ El daño no puede ser negativo. Se usará 0.")
            daño_base = 0
    except ValueError:
        print("❌ Ingresa un valor numérico válido.\n")
        continue

    # Fuerza del personaje
    entrada2 = input("Fuerza del personaje: ").strip()
    if entrada2.lower() == 'salir':
        print("¡Hasta luego, guerrero!")
        break
    try:
        fuerza = float(entrada2)
        if fuerza < 0:
            print("⚠️ La fuerza no puede ser negativa. Se usará 0.")
            fuerza = 0
    except ValueError:
        print("❌ Ingresa un valor numérico válido.\n")
        continue

    # ¿Ataque crítico?
    entrada3 = input("¿Ataque crítico? (s/n): ").strip()
    if entrada3.lower() == 'salir':
        print("¡Hasta luego, guerrero!")
        break

    # Bonificación elemental
    entrada4 = input("Bonificación elemental (fuego/hielo/rayo/ninguna): ").strip()
    if entrada4.lower() == 'salir':
        print("¡Hasta luego, guerrero!")
        break

    # --- CÁLCULOS ---
    
    # 1. Daño bruto con fuerza
    bono_fuerza = daño_base * fuerza * 0.05
    daño_bruto = daño_base + bono_fuerza
    
    # 2. Multiplicador crítico
    if entrada3.lower() == 's':
        multiplicador = 2.0
        es_critico = True
    else:
        multiplicador = 1.0
        es_critico = False
    
    # 3. Bonificación elemental
    if entrada4.lower() in ['fuego', 'hielo', 'rayo']:
        bonificacion_elemental = 0.20  # 20%
        elemento = entrada4.lower()
    else:
        bonificacion_elemental = 0
        elemento = "ninguna"
    
    # 4. Daño final
    daño_critico = daño_bruto * multiplicador
    daño_final = daño_critico * (1 + bonificacion_elemental)
    
    # --- MOSTRAR RESULTADOS ---
    print("\n" + "="*40)
    print("💥 RESULTADO DEL ATAQUE 💥")
    print("="*40)
    print(f"⚔️ Daño base: {daño_base:.2f}")
    print(f"💪 Bono fuerza ({fuerza} pts → +{fuerza*5:.0f}%): +{bono_fuerza:.2f}")
    print(f"🔪 Daño bruto: {daño_bruto:.2f}")
    
    if es_critico:
        print(f"✨ Crítico (x2.0): +{daño_bruto:.2f}")
    else:
        print(f"⚔️ Ataque normal: +0.00")
    
    if elemento != "ninguna":
        bono_elemental = daño_critico * bonificacion_elemental
        print(f"🔥 Bono {elemento} (+20%): +{bono_elemental:.2f}")
    
    print(f"\n💥 DAÑO TOTAL: {daño_final:.2f}")
    print("="*40)
    
    # --- REPETIR ---
    repetir = input("\n¿Calcular otro ataque? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n🏆 ¡Buena cacería, guerrero! 🏆")
        break
    
    print()