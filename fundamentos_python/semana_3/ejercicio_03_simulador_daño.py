"""Simulador de daño por enemigos:
Escribe un programa que simule un combate contra múltiples enemigos usando un bucle While principal y un for para los ataques.
1. Preguntar al jugador cuántos enemigos enfrentará.
2. Preguntar la vida inicial del jugador (50 - 200)
3. Para cada enemigo:
- El enemigo tiene vida aleatoria entre 20 y 60.
- Mostrar "Enemigo X aparece con Y de vida."
- Iniciar combate: 
    - El jugador ataca primero.
    - El enemigo contraataca.
    - Mostrar el daño causado y recibido.
    - Si el jugador o el enemigo llegan a 0 de vida, termina ese combate.
4. Acumulador del jugador:
- Si el jugador muere --> "GAME OVER" y terminar todo.
- Si el jugador sobrevive al enemigo --> vida restante, seguir al siguiente.
5. Al final, mostrar:
- Enemigos derrotados.
- Vida restante.
- Mensaje de victoria o derrota."""
import random

print("\n=== SIMULADOR DE COMBATE VS ENEMIGOS ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Número de enemigos
    entrada_enemigos = input("Número de enemigos a enfrentar (1-5): ").strip()
    if entrada_enemigos.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    try:
        numero_enemigos = int(entrada_enemigos)
        if numero_enemigos < 1 or numero_enemigos > 5:
            print("El número de enemigos debe estar entre 1 y 5.\n")
            continue
    except ValueError:
        print("Ingrese un número válido.\n")
        continue
    
    # Vida inicial del jugador
    entrada_vida = input("Vida inicial (50-200): ").strip()
    if entrada_vida.lower() == 'salir':
        print("¡Hasta luego, guerrero!")
        break
    
    try:
        vida_jugador = float(entrada_vida)
        if vida_jugador < 50 or vida_jugador > 200:
            print("La vida debe estar entre 50 y 200.\n")
            continue
    except ValueError:
        print("Ingrese un número válido.\n")
        continue
    
    # Inicializamos variables
    enemigos_derrotados = 0
    combate_terminado = False
    
    # Generamos enemigos con ciclo for
    for i in range(1, numero_enemigos + 1):
        if combate_terminado:
            break
            
        vida_enemigo = random.randint(20, 60)
        nombre_enemigo = random.choice(["Goblin", "Orco", "Esqueleto", "Trasgo", "No-muerto"])
        
        print(f"\nENEMIGO {i}: {nombre_enemigo} aparece con {vida_enemigo} de vida.")
        print(f"Tu vida: {vida_jugador}\n")
        
        # Inicia combate vs Enemigo
        while vida_enemigo > 0 and vida_jugador > 0:
            # Turno del jugador
            daño_jugador = random.randint(10, 30)
            vida_enemigo -= daño_jugador
            print(f"Atacas y causas {daño_jugador} de daño.")
            
            if vida_enemigo <= 0:
                print(f"¡{nombre_enemigo} ha sido derrotado!\n")
                enemigos_derrotados += 1
                break
            
            print(f"   Enemigo tiene {vida_enemigo} de vida restante.")
            
            # Turno del enemigo
            daño_enemigo = random.randint(5, 20)
            vida_jugador -= daño_enemigo
            print(f"{nombre_enemigo} te ataca y causa {daño_enemigo} de daño.")
            
            if vida_jugador <= 0:
                print(f"¡Has sido derrotado por {nombre_enemigo}!\n")
                combate_terminado = True
                break
            
            print(f"   Tu vida restante: {vida_jugador}\n")
    
    # --- RESULTADO FINAL ---
    print("\n" + "="*40)
    print("RESUMEN DEL COMBATE")
    print("="*40)
    print(f"Enemigos derrotados: {enemigos_derrotados}")
    print(f"Vida restante del jugador: {max(0, vida_jugador):.0f}")
    
    if enemigos_derrotados == numero_enemigos:
        print("\n¡VICTORIA! Derrotaste a todos los enemigos. ")
    elif combate_terminado:
        print("\nDERROTA. El mundo necesita un héroe más fuerte... ")
    
    # --- REPETIR ---
    repetir = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Gracias por jugar! Hasta la próxima, guerrero. ")
        break
    
    print()