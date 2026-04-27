""" Escribe un programa que simule el estado de un personaje después de recibir un golpe y evaluar condiciones.

Enunciado:
1. Preguntar la vida actual del personaje.
2. Preguntar si tiene escudo activo (s o n).
3. Preguntar si tiene veneno activo (s o n).

Calcular el estado final según:

1. Si vida <= 0 → "Derrotado"
2. Si vida < 30 → "Crítico"
3. Si vida >= 30 y tiene veneno → "Envenenado"
4. Si tiene escudo activo y vida > 0 → "Protegido"
5. Si ninguna condición especial → "Saludable"

Mostrar el estado final.

Validar que la vida no sea negativa (usar raise).

Repetir hasta que el usuario escriba "salir"."""

print("\n === SISTEMA DE ESTADO DE PERSONAJE ===\n")
print("Escriba 'salir' para cerrar el programa.")

while True:

    # 1. Vida actual del personaje
    entrada_vida = input("Vida actual del personaje: ").strip()
    if entrada_vida.lower() == 'salir':
        print("Sales sin validar el estado del personaje.")
        break
    try:
        vida_actual = float(entrada_vida)
        if vida_actual < 0:
            raise ValueError("La vida del personaje no puede ser menor que 0.")
    except ValueError as e:
        print(f"Error: {e}")
        continue
    # Escudo activo
    entrada_escudo = input("¿Tiene escudo? (s/n): ").strip().lower()
    if entrada_escudo == 'salir':
        print("Saliste sin validar el estado del personaje.")
        break
    if entrada_escudo == 's':
        escudo_activo = True
    else:
        escudo_activo = False
    # Tiene veneno activo
    entrada_veneno = input("¿Tiene veneno activo? (s/n): ").strip().lower()
    if entrada_veneno == 'salir':
        print("Saliste sin validar el estado del personaje.")
        break
    if entrada_veneno == 's':
        veneno_activo = True
    else:
        veneno_activo = False
    # Condiciones de estado
    if vida_actual <= 0:
        estado = 'Derrotado'
    elif vida_actual < 30:
        estado = 'Crítico'
    elif vida_actual >= 30 and veneno_activo:
        estado = 'Envenenado'
    elif vida_actual > 0 and escudo_activo:
        estado = 'Protegido'
    else:
        estado = 'saludable'
    #Mostramos estado
    print(f"Estado ---> {estado}")

    # Otro estado
    repetir = input("\n¿Calcular otro estado? (s/n): ").strip().lower()
    if repetir != 's':
        print("Hasta la próxima!")
        break

    print()