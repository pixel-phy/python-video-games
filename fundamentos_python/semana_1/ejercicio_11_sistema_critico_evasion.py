""" Escribe un programa para un juego RPG que simule un ataque con posibilidad de crítico y evasión.
1. Preguntar el daño base del atacante (número decimal).
2. Preguntar la probabilidad de crítico (0 a 100%).
3. Preguntar la probabilidad de evasión del defensor (0 a 100%).
4. Calcular si el ataque es crítico o no:
- Generar un número aleatorio entre 1 y 100
- Si es menor o igual a la probabilidad de crítico → daño × 2

5. Calcular si el defensor evade:
- Generar otro número aleatorio:
- Si evade → daño final = 0
- Mostrar el resultado detallado.

6. Repetir hasta que el usuario escriba "salir".
"""
import random

print("\n=== SISTEMA CRÍTICO Y EVASIÓN ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # --- DAÑO BASE ---
    entrada1 = input("Daño base del atacante: ").strip()
    if entrada1.lower() == 'salir':
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    
    try:
        daño_base = float(entrada1)
        if daño_base <= 0:
            raise ValueError("El daño debe ser mayor a 0")
    except ValueError as e:
        print(f"Error: {e}\n")
        continue

    # --- PROBABILIDAD DE CRÍTICO ---
    entrada2 = input("Probabilidad de crítico (0-100): ").strip()
    if entrada2.lower() == 'salir':
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    
    try:
        prob_critico = int(entrada2)
        if prob_critico < 0 or prob_critico > 100:
            raise ValueError("La probabilidad debe estar entre 0 y 100")
    except ValueError as e:
        print(f"Error: {e}\n")
        continue

    # --- PROBABILIDAD DE EVASIÓN ---
    entrada3 = input("Probabilidad de evasión (0-100): ").strip()
    if entrada3.lower() == 'salir':
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    
    try:
        prob_evasion = int(entrada3)
        if prob_evasion < 0 or prob_evasion > 100:
            raise ValueError("La probabilidad debe estar entre 0 y 100")
    except ValueError as e:
        print(f"Error: {e}\n")
        continue

    # --- TIRADAS ---
    tirada_critico = random.randint(1, 100)
    tirada_evasion = random.randint(1, 100)
    
    # --- CALCULAR CRÍTICO ---
    if tirada_critico <= prob_critico:
        daño_parcial = daño_base * 2
        es_critico = True
    else:
        daño_parcial = daño_base
        es_critico = False
    
    # --- CALCULAR EVASIÓN ---
    if tirada_evasion <= prob_evasion:
        daño_final = 0
        evade = True
    else:
        daño_final = daño_parcial
        evade = False
    
    # --- MOSTRAR RESULTADOS ---
    print("\n--- RESULTADO ---")
    print(f"Daño base: {daño_base:.0f}")
    print(f"Tirada de crítico: {tirada_critico}")
    
    if es_critico:
        print("¡CRÍTICO! (x2)")
    else:
        print("Ataque normal")
    
    print(f"Tirada de evasión: {tirada_evasion}")
    
    if evade:
        print("¡EL DEFENSOR EVADIÓ! Daño: 0")
    else:
        print(f"Daño final: {daño_final:.0f}")
    
    # --- REPETIR ---
    repetir = input("\n¿Calcular otro ataque? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Buena partida! Hasta la próxima.")
        break
    
    print()