"""Sistema de combate por turnos (versión completa)
Escribe un programa que simule un combate por turnos entre un jugador y un enemigo, con las giuientes características:
1. Creación del jugador:
- Preguntar nombre.
- Preguntar vida (50 - 150)
- Preguntar fuerza (10 - 30)
2. Generación del enemigo (aleatoria):
- Nombre aleatorio de una lista.
- Vida aleatoria (30 - 100).
- Fuerza aleatoria (8 - 25).
3. Sistema de combate por turnos:
- Mostrar siempre la vida de ambos.
- El jugador elige entre:
1. Atacar: daño = fuerza del jugador + (1 a 10 extra).
2. Usar poción: cura 20 % de la vida máxima (sin superarla).
3. Huir: 50 % de probabilidad de éxito.
- El enemigo ataca automáticamente después del jugador.
4. Condiciones de fin:
- Jugador o enemigo con vida <= 0
- El jugador huye con éxito.
5. Validaciones:
- Usar try/except para opciones del menú
- Usar raise para validar vida y fuerza
- Permitir "salir" en cualquier momento.
6. Bucle principal
- Un while para el combate.
- Otro while externo para repetir la partida."""

import random

print("\n=== SISTEMA DE COMBATE POR TURNOS ===\n")

while True:
    # --- CREACIÓN DEL JUGADOR ---
    print("\n--- CREACIÓN DEL JUGADOR ---")
    
    nombre = input("Nombre: ").strip()
    if nombre.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    if not nombre:
        print("El nombre no puede ir vacío.\n")
        continue
    
    # Vida del jugador
    while True:
        try:
            vida_max = float(input("Vida (50-150): "))
            if vida_max < 50 or vida_max > 150:
                raise ValueError("La vida debe estar entre 50 y 150")
            break
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    # Fuerza del jugador
    while True:
        try:
            fuerza = float(input("Fuerza (10-30): "))
            if fuerza < 10 or fuerza > 30:
                raise ValueError("La fuerza debe estar entre 10 y 30")
            break
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    vida_actual = vida_max
    
    # --- GENERACIÓN DEL ENEMIGO ---
    print("\n--- GENERACIÓN DEL ENEMIGO ---")
    nombres_enemigo = ["Orco", "Goblin", "Esqueleto", "Trasgo", "No-muerto"]
    enemigo = random.choice(nombres_enemigo)
    vida_enemigo = random.randint(30, 100)
    fuerza_enemigo = random.randint(8, 25)
    
    print(f"\n¡Aparece un {enemigo}!")
    print(f"Vida: {vida_enemigo} | Fuerza: {fuerza_enemigo}")
    
    # --- COMBATE ---
    turno = 1
    huir = False
    
    while not huir and vida_actual > 0 and vida_enemigo > 0:
        print(f"\n--- TURNO {turno} ---")
        print(f"{nombre}: {vida_actual:.0f}/{vida_max:.0f}")
        print(f"{enemigo}: {vida_enemigo:.0f}")
        
        print("\n¿Qué haces?")
        print("1. Atacar")
        print("2. Usar poción")
        print("3. Huir")
        
        accion = input("Elige: ").strip()
        
        # --- ATAQUE DEL JUGADOR ---
        if accion == '1':
            daño = fuerza + random.randint(1, 10)
            vida_enemigo -= daño
            print(f"¡Atacas y causas {daño:.0f} de daño!")
            
            if vida_enemigo <= 0:
                print(f"\n✨ ¡{enemigo} ha sido derrotado! ✨")
                break
        
        # --- USAR POCIÓN ---
        elif accion == '2':
            curacion = vida_max * 0.2
            vida_actual += curacion
            if vida_actual > vida_max:
                vida_actual = vida_max
            print(f"Usas una poción. Recuperas {curacion:.0f} de vida.")
        
        # --- HUIR ---
        elif accion == '3':
            if random.choice([True, False]):  # 50% probabilidad
                print("Lograste escapar con vida!")
                huir = True
                break
            else:
                print("Fallaste al huir. El enemigo te ataca de inmediato!")
        
        else:
            print("Acción no válida. Pierdes el turno.")
        
        # --- ATAQUE DEL ENEMIGO (si sigue vivo) ---
        if not huir and vida_enemigo > 0 and vida_actual > 0:
            daño_enemigo = random.randint(5, fuerza_enemigo + 5)
            vida_actual -= daño_enemigo
            print(f"{enemigo} te ataca y causa {daño_enemigo:.0f} de daño.")
            
            if vida_actual <= 0:
                print(f"\n¡Has sido derrotado por {enemigo}!")
                break
        
        turno += 1
    
    # --- RESULTADO FINAL ---
    print("COMBATE FINALIZADO")
    
    if vida_actual <= 0:
        print(f"Derrota. {nombre} ha caído ante {enemigo}.")
    elif vida_enemigo <= 0:
        print(f"¡Victoria! {nombre} derrotó a {enemigo}.")
    elif huir:
        print(f"{nombre} huyó del combate con {vida_actual:.0f} de vida restante.")
    
    print(f"Vida restante: {max(0, vida_actual):.0f}/{vida_max:.0f}")
    print(f"Turnos totales: {turno}")
    
    # --- REPETIR ---
    repetir = input("\n¿Jugar otra partida? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Gracias por jugar!")
        break
    
    print()