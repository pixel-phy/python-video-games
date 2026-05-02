"""Game loop básico:
Escribe un programa que simule el bucle principal de un juego RPG:
1. El jugador comienza con 3 vidas.
2. En cada iteración del bucle:
- Mostrar vidas restantes.
- Preguntar: ¿Quieres seguir jugando? (s/n)
- Si responde "s", continúa.
- Si responde "n", rompe el bucle y termina el juego.
- Si responde algo diferente, mostar mensaje de error y no gastar vida.
3. Si el jugador pierde una vida (Por ejemplo, si elige una opción inválida que sí la gaste), reducir vidas.
4. Cuando llegue a 0 vidas, mostrar "Game Over" y terminar.
5. Permitir salir con "salir". """

print("\n=== GAME LOOP RPG ===\n")
vidas = 3
game_over = False  # Bandera para saber si perdió o salió voluntariamente

while vidas > 0:
    print(f"\nTienes {vidas} vidas. Escribe 'salir' para terminar.\n")
    print(f"❤️ Vidas restantes: {vidas}")
    pregunta = input("¿Quieres seguir jugando? (s/n): ").strip().lower()
    
    if pregunta == 'salir':
        print("Has terminado el juego voluntariamente.")
        break
    
    elif pregunta == 's':
        print("⚔️ Continúa la aventura...")
    
    elif pregunta == 'n':
        print("Has terminado el juego voluntariamente.")
        break
    
    else:
        # Validar si es un número negativo
        try:
            numero = float(pregunta)
            if numero < 0:
                print("❌ Número negativo no es una opción válida. ¡Pierdes una vida!")
                vidas -= 1
                if vidas == 0:
                    game_over = True
                continue
            else:
                print("❌ Opción no válida. ¡No pierdes vida!")
                continue
        except ValueError:
            print("❌ Opción no válida. ¡No pierdes vida!")
            continue
    
# Mostrar resultado final
if vidas == 0 or game_over:
    print(f"\n💀 ¡GAME OVER! Te quedaste sin vidas. 💀")
else:
    print(f"\n👋 ¡Hasta luego! Terminaste el juego con {vidas} vidas restantes.")