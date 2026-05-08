""" Sistema de selección de clase RPG
Escribe un programa que ayude a un jugador a elegir su clase según sus estadísticas y preferencias.
Enunciado:
1. Preguntar el nombre del personaje.
2. Preguntar su estilo de juego preferido:

"cuerpo a cuerpo" → Guerrero / Monje
"distancia" → Arquero / Mago

Preguntar su atributo principal:
Si eligió "cuerpo a cuerpo" → preguntar: "fuerza" o "velocidad"
Si eligió "distancia" → preguntar: "puntería" o "magia"

Asignar la clase según las respuestas:

Estilo	                    Atributo	                     Clase
cuerpo a cuerpo	            fuerza	                         Guerrero 🛡️
cuerpo a cuerpo	            velocidad	                    Monje 🥋
distancia	                puntería	                    Arquero 🏹
distancia	                    magia	                        Mago 🔮

Mostrar un mensaje de presentación de la clase.
Preguntar si quiere crear otro personaje.
Repetir hasta que el usuario escriba "salir"."""
print("\n=== SISTEMA DE SELECCIÓN DE CLASE PARA JUEGO RPG ===\n")
print("(Escribe 'salir' para finalizar el programa)\n")

while True:
    # Nombre del personaje 
    nombre_original = input("Nombre del personaje: ").strip()
    if nombre_original.lower() == 'salir':
        print("¡Hasta luego, aventurero!")
        break
    
    nombre_personaje = nombre_original 
    
    # Estilo de juego
    estilos_validos = ['cuerpo a cuerpo', 'distancia']
    estilo_favorito = input("Estilo de juego (cuerpo a cuerpo / distancia): ").strip().lower()
    
    if estilo_favorito == 'salir':
        print("¡Hasta luego, aventurero!")
        break
    
    try:
        if estilo_favorito not in estilos_validos:
            raise ValueError(f"El estilo '{estilo_favorito}' no existe.")
    except ValueError as e:
        print(f"❌ Error: {e}")
        continue
    
    # Atributo según estilo
    if estilo_favorito == 'cuerpo a cuerpo':
        atributos_validos = ['fuerza', 'velocidad']
        atributo_favorito = input("Atributo principal (fuerza / velocidad): ").strip().lower()
    else:  # distancia
        atributos_validos = ['punteria', 'magia']
        atributo_favorito = input("Atributo principal (punteria / magia): ").strip().lower()
    
    try:
        if atributo_favorito not in atributos_validos:
            raise ValueError(f"El atributo '{atributo_favorito}' no es válido.")
    except ValueError as e:
        print(f"❌ Error: {e}")
        continue
    
    # Asignar clase y descripción
    if estilo_favorito == 'cuerpo a cuerpo':
        if atributo_favorito == 'fuerza':
            clase = "Guerrero 🛡️"
            descripcion = "confía en su fuerza bruta para aplastar enemigos."
        else:
            clase = "Monje 🥋"
            descripcion = "usa su velocidad y agilidad para golpear múltiples veces."
    else:  # distancia
        if atributo_favorito == 'punteria':
            clase = "Arquero 🏹"
            descripcion = "derriba enemigos desde lejos con su arco."
        else:
            clase = "Mago 🔮"
            descripcion = "canaliza poderes arcanos para devastar al enemigo."
    
    # Mostrar resultado
    print(f"\n¡{nombre_personaje} ha sido elegido como {clase}!")
    print(f"Un {clase.split()[0]} {descripcion}\n")
    
    # Repetir
    repetir = input("¿Crear otro personaje? (s/n): ").strip().lower()
    if repetir != 's':
        print("\n¡Gracias por jugar! Hasta la próxima, aventurero. 🎮")
        break
    
    print()