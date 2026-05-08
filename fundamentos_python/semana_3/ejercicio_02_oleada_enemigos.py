"""Oleada de enemigos:
Escribir un programa que simula la generación de una oleada de enemigos en un juego RPG.
1. Preguntar al jugador cuántos enemigos tendrá la oleada (número entero entre 1 y 10).
2. Preguntar el nombre del enemigo ("goblin", "orco", "esqueleto").
3. Usar un bucle for para generar cada enemigo con:
- Vida aleatoria entre 20 y 50.
- Daño aleatorio entre 5 y 15.
4. Mostrar las estadísticas de cada enemigo.
5. Al final, mostrar resumen:
- Total de enemigos generados. 
- Vida total de la oleada (Suma de vidas).
- Daño promedio de los enemigos.
6. Preguntar si quiere generar otra oleada.
7. Repetir hasta que el usuario escriba salir."""
import random

print("\n=== OLEADA DE ENEMIGOS ===\n")
print("(Escribe 'salir' para terminar)\n")

while True:
    # Cantidad de enemigos
    pregunta1 = input("¿Cuántos enemigos tendrá la oleada (1-10)?: ").strip()
    if pregunta1.lower() == 'salir':
        print("Has salido de la partida. ¡Hasta la próxima!")
        break
    
    try:
        oleada_enemiga = int(pregunta1)
        if oleada_enemiga < 1 or oleada_enemiga > 10:
            print("❌ La oleada debe estar entre 1 y 10.\n")
            continue
    except ValueError:
        print("❌ Ingrese un número válido.\n")
        continue
    
    # Tipo de enemigo
    nombre_enemigo = input("Escriba el tipo de enemigo ('goblin', 'orco', 'esqueleto'): ").strip().lower()
    if nombre_enemigo == 'salir':
        print("Has salido de la partida. ¡Hasta la próxima!")
        break
    
    while nombre_enemigo not in ['goblin', 'orco', 'esqueleto']:
        print("❌ Opción no válida.")
        nombre_enemigo = input("Tipo de enemigo ('goblin', 'orco', 'esqueleto'): ").strip().lower()
        if nombre_enemigo == 'salir':
            print("Has salido de la partida. ¡Hasta la próxima!")
            break
    if nombre_enemigo == 'salir':
        break
    
    # Inicializar acumuladores
    suma_vida_enemigos = 0
    suma_daño_enemigos = 0
    
    print(f"\n--- OLEADA DE {nombre_enemigo.upper()}S ---")
    
    # Generar enemigos
    for i in range(1, oleada_enemiga + 1):
        vida_enemigo = random.randint(20, 50)
        daño_enemigo = random.randint(5, 15)
        print(f"{nombre_enemigo.capitalize()} {i}: ❤️ Vida: {vida_enemigo} | ⚔️ Daño: {daño_enemigo}")
        
        suma_vida_enemigos += vida_enemigo
        suma_daño_enemigos += daño_enemigo
    
    # Calcular promedio
    promedio_daño = suma_daño_enemigos / oleada_enemiga
    
    # Mostrar resumen
    print("\n--- RESUMEN ---")
    print(f"Total enemigos generados: {oleada_enemiga}")
    print(f"Vida total de la oleada: {suma_vida_enemigos}")
    print(f"Daño promedio de los enemigos: {promedio_daño:.2f}")
    
    # Repetir
    repetir = input("\n¿Generar otra oleada? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Hasta la próxima, comandante!")
        break
    
    print()