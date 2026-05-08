"""Crearás un programa donde:
1. El jugador crea su personaje (nombre, vida, fuerza)
2. El enemigo se genera automáticamente (vida y fuerza aleatoria)
3. Se desarrolla un combate por turnos:
- Jugador ataca primero
- Enemigo contraataca
4. Opciones del jugador: Atacar / Usar poción / Huir

El combate termina cuando alguien muere o el jugador huye"""
import random
import time
print("\n=== Proyecto integrador: Simulador de combate ===\n")
print("Escribe 'salir' para terminar.\n ")

while True:
    # Creación del personaje.
    # 1.1 Nombre
    nombre_personaje = input("Nombre del personaje: ").strip().lower()
    if nombre_personaje == 'salir':
        print("Te has retirado del combate.")
        break
    # 1.2 Vida
    entrada_vida = input("Vida del personaje: ").strip()
    if entrada_vida.lower() == 'salir':
        print("Te has retirado del combate.")
        break
    try:
        vida_personaje = float(entrada_vida)
        if vida_personaje > 150 or vida_personaje <= 0:
            raise ValueError("La vida debe ser mayor que 0 y menor o igual que 150.\n")
    except ValueError as e:
        print(f"Error: {e}.")
        continue
    # 1.3 Fuerza 
    try:
        fuerza_personaje = float(input("Fuerza del personaje: "))
        if fuerza_personaje == 'salir':
            print("Te has retirado del combate.")
            break
        if fuerza_personaje <= 0 or fuerza_personaje >= 100:
            raise ValueError("La fuerza debe ser un valor entre 0 y 100.")
    except ValueError:
        print("Ingrese un valor numérico válido.")
        continue

    # Generación del enemigo con estadísticas aleatorias.
    # 2.1 Creación nombre aleatorio
    opciones_nombres_enemigo = ["Agnus", "Verstralung", "Arnuld"]
    nombre_enemigo = random.choice(opciones_nombres_enemigo)
    # 2.2 Vida y fuerzas aleatorias
    vida_enemigo = random.randint(100, 130)
    fuerza_enemigo = random.randint(60,80)

    # Inicia el turno 1
    turno = 1

    print(f"{nombre_personaje} se enfreta a {nombre_enemigo}!")
    print(f"{nombre_personaje} tiene {vida_personaje} puntos de vida | {nombre_enemigo} tiene {vida_enemigo} puntos de vida")

    while vida_personaje > 0 and vida_enemigo > 0:
        print(f"\n--- TURNO {turno} ---")
        # Turno del jugador
        print("\n TU TURNO")
        accion = input("Qué acción deseas hacer (atacar, usar pocion, huir): ").strip().lower()
        if accion == 'atacar':
            vida_enemigo -= fuerza_personaje
            print(f"Atacas a {nombre_enemigo}, causas {fuerza_personaje} de daño.")
        elif accion == 'usar pocion':
            curacion = random.randint(50,100)
            vida_personaje += curacion
            if vida_personaje >= 150:
                vida_personaje = 150
                print(f"Te curas {curacion} puntos de vida. Ahora tienes {vida_personaje}.")
        elif accion == 'huir':
            print("Has huido del combate.")
            break
        else:
            print("Acción no reconocida. Pierdes el turno.")

        if vida_enemigo <= 0:
            break

        # Turno del enemigo
        print(f"Turno de {nombre_enemigo}")
        time.sleep(2) # Pausa para dar emoción al combate

        daño_enemigo = random.randint(10, fuerza_enemigo)
        vida_personaje -= fuerza_enemigo
        print(f"{nombre_enemigo} te ataca y causa {fuerza_enemigo} de daño.")

        # Mostrar estadísticas actuales
        print(f"{nombre_personaje}: {vida_personaje} | {nombre_enemigo}: {vida_enemigo}")
        turno += 1
        time.sleep(1.5)

    #Resultado final
    print("¡Batalla finalizada!")
    if vida_personaje <= 0:
        print(f"{nombre_personaje} ha sido derrotado por {nombre_enemigo}!")
        print("GAME OVER!")
    elif accion == 'huir':
        print()
    else:
        print(f"¡En hora buena! {nombre_personaje} derrotó a {nombre_enemigo}.")
    
    print(f"Total de turnos: {turno}")

    # Seguir jugando
    repetir = input("\n¿Jugar otro combate? (s/n): ").strip().lower()
    if repetir != 's':
        print("Buen juego. Hasta la próxima.")
        break