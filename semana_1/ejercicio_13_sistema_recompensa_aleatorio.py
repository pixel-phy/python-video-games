"""Escribe un programa que simule una recompensa aleatoria al derrotar un enemigo.
1. Generar aleatoriamente un número del 1 al 100 (el "botín").
2. Determinar la recompensa según:
. 1-20 → Poción común (+20 de vida)
. 21-50 → Poción grande (+50 de vida)
. 51-75 → Poción mega (+100 de vida)
. 76-90 → Objeto épico (espada, armadura o casco)
. 91-100 → ¡Tesoro legendario!

3. Preguntar si el jugador quiere abrir el botín o guardarlo para después.
- Si abre → mostrar recompensa
- Si guarda → mostrar mensaje "Botín guardado para después"

4. Mostrar en detalle qué obtuvo.
5. Preguntar si quiere otro botín.
6. Repetir hasta que escriba "salir". """

import random

print("\n=== SISTEMA DE RECOMPENSA ALEATORIA ===\n")
print("(Escribe 'salir' en cualquier momento para terminar)\n")

while True:
    # Genero el botín
    tirada = random.randint(1, 100)
    
    if tirada >= 1 and tirada <= 20:
        nivel = "COMÚN"
        recompensa = "Poción común (+20 de vida)"
        valor_vida = 20
    elif tirada >= 21 and tirada <= 50:
        nivel = "GRANDE"
        recompensa = "Poción grande (+50 de vida)"
        valor_vida = 50
    elif tirada >= 51 and tirada <= 75:
        nivel = "MEGA"
        recompensa = "Poción mega (+100 de vida)"
        valor_vida = 100
    elif tirada >= 76 and tirada <= 90:
        nivel = "ÉPICO"
        opciones_epicas = ["Espada épica", "Armadura épica", "Casco épico"]
        recompensa = random.choice(opciones_epicas)
        valor_vida = 0
    else:  # 91-100
        nivel = "LEGENDARIO"
        opciones_legendarias = ["Espada legendaria", "Armadura legendaria", "Casco legendario"]
        recompensa = random.choice(opciones_legendarias)
        valor_vida = 0
    
    print(f"\nTirada: {tirada}")
    print(f"¡Nivel {nivel}! ➡️ {recompensa}")
    
    # Abrir o guardar
    pregunta = input("\n¿Quieres 'abrir' el botín o 'guardar' para después? (o 'salir'): ").strip().lower()
    
    if pregunta == 'salir':
        print("\n¡Hasta luego, aventurero!")
        break
    elif pregunta == 'abrir':
        if valor_vida > 0:
            print(f"¡Abriste el botín! Recibes: {recompensa}")
        else:
            print(f"¡Abriste el botín! Obtienes: {recompensa}")
    elif pregunta == 'guardar':
        print("Botín guardado para después.")
    else:
        print("Opción no válida. El botín se pierde...")
    
    # --- REPETIR ---
    repetir = input("\n¿Quieres otro botín? (s/n): ").strip().lower()
    if repetir == 'salir' or repetir != 's':
        print("\n¡Gracias por jugar! Hasta la próxima.")
        break
    
    print()