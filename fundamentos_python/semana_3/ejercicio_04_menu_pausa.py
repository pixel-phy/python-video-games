"""Menú de pausa de juego
Escribe un programa que simule un menú de pausa durante una partida.
1. Mostrar un mensaje: "Juego en curso... (presiona P para pausar)". 
2. Simular un bucle de juego que cuenta segundos de juego (solo incrementa un contador).
3. El usuario puede escribir "P" o "p" para abrir el menú de pausa.
4. En el menú de pausa, mostrar las opciones:
- 1. Reaundar partida.
- 2. Ver estadísticas.
- 3. Salir del juego."""

enemigos = 0
opcion2 = ""

while True:
    print("\n=== JUEGO RPG ===")

    if opcion2 != "salir":
        opcion2 = input("'p' para pausar, 'e' para derrotar enemigo, 'salir' para terminar: ").strip().lower()
        if opcion2 == 'p':
            print("\n=== MENÚ PAUSA ===")
            print("1. Reanudar partida")
            print("2. Ver estadísticas")
            print("3. Salir del juego")

            while True:
                opcion3 = input("\nIngrese opción: ")
                if opcion3 == "1":
                    print("La partida continúa: ")
                    break
                elif opcion3 == "2":
                    print(f"Has derrotado {enemigos} enemigos.")
                    continue
                elif opcion3 == "3":
                    opcion2 = "salir"
                    break
                else:
                    print("Ingrese una opción válida")
                    continue

        elif opcion2 == "e":
            enemigos += 1
            print(f"\nEnemigo derrotado: {enemigos}")
            continue
        elif opcion2 == "salir":
            print(f"Partida terminada! Derrotaste: {enemigos} enemigos")
            break
        else:
            print("Ingrese una opción válida")
            continue
    else:
        print(f"Partida terminada! Derrotaste: {enemigos} enemigos")
        break


