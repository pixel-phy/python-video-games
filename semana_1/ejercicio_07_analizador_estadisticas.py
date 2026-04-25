""" Escribe un programa para un juego RPG que:
1. Pregunte al usuario una estadística de un personaje (puede ser un número entero, decimal, texto, "True" o "False").
2. Detecte automáticamente qué tipo de estadística es:
- int (entero): ejemplo nivel = 5
- float (decimal): ejemplo fuerza = 12.7
- str (texto): ejemplo nombre = "Héctor"
- bool (booleano): ejemplo es_mago = True

3. Muestre el tipo detectado y el valor original.
4. Intente convertir esa estadística a los otros tres tipos y muestre:
- El resultado de la conversión, o "No aplica" si no se puede o no tiene sentido (ej: convertir un nombre a número).

Repita hasta que el usuario escriba "fin"."""
print("\n### ANALIZADOR DE ESTADÍSTICAS RPG ###\n")
print("(Escribe 'fin' para finalizar)")

while True:
    entrada = input("\nIngresa una estadística del personaje: ").strip()
    
    if entrada.lower() == 'fin':
        print("\n¡Gracias por usar el analizador! Hasta la próxima.")
        break
    
    # --- DETECCIÓN DE TIPO ---
    
    # Caso 1: Booleano
    if entrada.lower() == 'true':
        tipo_original = bool
        valor_original = True
    elif entrada.lower() == 'false':
        tipo_original = bool
        valor_original = False
    else:
        # Caso 2: Entero (sin punto decimal)
        try:
            if '.' not in entrada:
                valor_original = int(entrada)
                tipo_original = int
            else:
                raise ValueError  # Si tiene punto, no es entero
        except ValueError:
            # Caso 3: Flotante
            try:
                valor_original = float(entrada)
                tipo_original = float
            except ValueError:
                # Caso 4: String (texto)
                valor_original = entrada
                tipo_original = str
    
    # --- MOSTRAR RESULTADOS ---
    print("\n--- Análisis de estadística ---")
    print(f"Valor original: {valor_original}")
    print(f"Tipo detectado: {tipo_original.__name__}")
    
    # --- CONVERSIONES ---
    
    # A entero
    if tipo_original == int:
        print(f"→ Como entero: {valor_original}")
    else:
        try:
            print(f"→ Como entero: {int(valor_original)}")
        except (ValueError, TypeError):
            print("→ Como entero: No aplica")
    
    # A float
    if tipo_original == float:
        print(f"→ Como float: {valor_original}")
    else:
        try:
            print(f"→ Como float: {float(valor_original)}")
        except (ValueError, TypeError):
            print("→ Como float: No aplica")
    
    # A string (siempre se puede)
    print(f"→ Como texto: \"{str(valor_original)}\"")
    
    # A booleano (siempre se puede, pero con reglas especiales)
    if isinstance(valor_original, str) and valor_original == "":
        print(f"→ Como booleano: False (string vacío)")
    else:
        print(f"→ Como booleano: {bool(valor_original)}")