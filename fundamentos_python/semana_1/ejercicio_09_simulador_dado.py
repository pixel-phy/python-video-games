"""El programa debe:
1. Preguntar al usuario cuántas caras tiene el dado (4, 6, 8, 10, 12, 20, etc.).
2.Preguntar si quiere tirar el dado ("tirar") o salir ("salir").
3. Simular una tirada de dado (número aleatorio entre 1 y el número de caras).
4. Mostrar el resultado de la tirada.
5. Asignar un botín según el resultado:
- Si saca el máximo (ej: 20 en un dado de 20): "¡Botín legendario! ⭐"
- Si saca más de la mitad (ej: >10 en dado de 20): "Botín épico 🏆"
- Si saca menos de la mitad: "Botín común 📦"
- Si saca 1 (el mínimo): "¡Oh no! Trampa enemiga 💀"
6. Preguntar si quiere tirar de nuevo.

Repetir hasta que el usuario quiera salir."""
import random

print("\n=== SIMULADOR DE DADO Y LOOT RPG ===\n")
print("(Escribe 'salir' en cualquier momento para terminar)\n")

while True:
    # --- NÚMERO DE CARAS DEL DADO ---
    entrada1 = input("¿Cuántas caras tiene el dado? (mínimo 2): ").strip()
    if entrada1.lower() == 'salir':
        print("¡Buena partida, aventurero! 🎲")
        break
    
    try:
        caras_dado = int(entrada1)
        if caras_dado < 2:
            print("❌ El dado debe tener al menos 2 caras.\n")
            continue
    except ValueError:
        print("❌ Ingresa un número entero válido.\n")
        continue

    # --- ACCIÓN DEL JUGADOR ---
    entrada2 = input("¿Quieres 'tirar' el dado o 'salir'?: ").strip().lower()
    
    if entrada2 == 'salir':
        print("¡Buena partida, aventurero! 🎲")
        break
    
    elif entrada2 == 'tirar':
        # Tirar el dado
        resultado = random.randint(1, caras_dado)
        print(f"\n🎲 TIRANDO DADO DE {caras_dado} CARAS...")
        print(f"¡Sacaste un {resultado}!")
        
        # Asignar botín
        print("-" * 30)
        if resultado == caras_dado:
            print("⭐ ¡BOTÍN LEGENDARIO! ¡Tesoro ancestral!")
        elif resultado > caras_dado / 2:
            print("🏆 ¡BOTÍN ÉPICO! ¡Espada de acero!")
        elif resultado == 1:
            print("💀 ¡TRAMPA ENEMIGA! Pierdes 10 de vida.")
        else:
            print("📦 BOTÍN COMÚN: 10 monedas de oro.")
        print("-" * 30)
        
        # Preguntar si repetir
        repetir = input("\n¿Tirar de nuevo? (s/n): ").strip().lower()
        if repetir != 's':
            print("\n🏆 ¡Buena cacería! Hasta la próxima. 🏆")
            break
        
        print()  # Línea en blanco
    
    else:
        print("❌ Opción no válida. Usa 'tirar' o 'salir'.\n")
        continue