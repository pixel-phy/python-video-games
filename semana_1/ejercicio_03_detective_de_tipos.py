""" Escribe un programa que:
Pida al usuario que ingrese un valor (puede ser cualquier cosa: número, texto, "True", "False").
1. Detecte automáticamente qué tipo de dato es:
int (entero)
float (decimal)
str (texto)
bool (booleano)

2. Muestre el tipo detectado y el valor original.

3. Intente convertir ese valor a los otros tres tipos y muestre:

4. El resultado de la conversión, o "No se puede convertir" si falla.
5. Repita hasta que el usuario escriba "fin". """

print("\n### Detective de tipos ###\n")

while True:
    print("Para salir escriba 'fin'.")
    entrada = input("Ingrese un valor: ")
    #Limpiamos espacios a la entrada.
    entrada_limpia = entrada.strip()

    if entrada_limpia.lower() == 'fin':
        print("Que estés muy bien!")
        break

    #Caso 1: Booleano
    if entrada_limpia.lower() == 'true':
        tipo_original = bool
        valor_original = True
    elif entrada_limpia.lower() == 'false':
        tipo_original = bool
        valor_original = False
    
    # Caso 2: Entero
    else:
        try:
            # Verificamos si es entero (sin punto decimal)
            if "." not in entrada_limpia:
                tipo_original = int
                valor_original = int(entrada_limpia)
            else:
                raise ValueError # Si tiene punto no es entero.
        except ValueError:
            # Caso 3: Float
            try:
                valor_original = float(entrada_limpia)
                tipo_original = float
            except ValueError:
                valor_original = entrada_limpia
                tipo_original = str

    # Mostramos resultados en pantalla:
    print("\n--- Análisis ---")
    print(f"Valor original: {valor_original}")
    print(f"Tipo detectado original: {tipo_original.__name__}")

    #Realizo conversiones
    #A entero
    if tipo_original == int:
        print(f"Como entero: {valor_original}")
    else:
        try:
            print(f"Como entero: {int(valor_original)}")
        except (ValueError, TypeError):
            print("Como entero no se puede convertir.")
    
    #A float
    if tipo_original == float:
        print(f"Como float: {valor_original}")
    else:
        try:
            print(f"Como float: {float(valor_original)}")
        except (ValueError, TypeError):
            print("Como float no se puede convertir.")
    
    #Como string
    print(f"Como string: {str(valor_original)}")

    #Como bool
    print(f"Como bool: {bool(valor_original)}")