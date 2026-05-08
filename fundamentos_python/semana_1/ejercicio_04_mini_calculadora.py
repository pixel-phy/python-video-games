""" Escribe un programa que:
1. Pida al usuario dos números (pueden ser enteros o decimales).
2. Pida al usuario una operación matemática:
+ (suma), - (resta), * (multiplicación), / (división), // (división entera), % (módulo o resto), ** (potencia).
3. Realice el cálculo y muestre el resultado con 2 decimales si es necesario.
4. Pregunte si quiere hacer otro cálculo (s para sí, n para no).
5. Repita hasta que el usuario responda "n". """

print("\n=== MINI CALCULADORA ===\n")
print("(Escribe 'n' en cualquier momento para salir)")

while True:
    # Primer número
    entrada1 = input("Ingresa el primer número: ")
    if entrada1.lower() == 'n':
        print("¡Hasta luego!")
        break
    try:
        num1 = float(entrada1)
    except ValueError:
        print("❌ Debes ingresar un número válido.\n")
        continue
    
    # Segundo número
    entrada2 = input("Ingresa el segundo número: ")
    if entrada2.lower() == 'n':
        print("¡Hasta luego!")
        break
    try:
        num2 = float(entrada2)
    except ValueError:
        print("❌ Debes ingresar un número válido.\n")
        continue
    
    # Operador
    operador = input("Operación (+, -, *, /, //, %, **): ").strip()
    if operador.lower() == 'n':
        print("¡Hasta luego!")
        break
    
    # Realizar cálculo
    if operador == '+':
        resultado = num1 + num2
        print(f"{num1:.2f} + {num2:.2f} = {resultado:.2f}")
    
    elif operador == '-':
        resultado = num1 - num2
        print(f"{num1:.2f} - {num2:.2f} = {resultado:.2f}")
    
    elif operador == '*':
        resultado = num1 * num2
        print(f"{num1:.2f} × {num2:.2f} = {resultado:.2f}")
    
    elif operador == '/':
        if num2 == 0:
            print("❌ Error: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print(f"{num1:.2f} / {num2:.2f} = {resultado:.2f}")
    
    elif operador == '//':
        if num2 == 0:
            print("❌ Error: No se puede dividir entre cero")
        else:
            resultado = num1 // num2
            print(f"{num1:.2f} // {num2:.2f} = {resultado}")
    
    elif operador == '%':
        if num2 == 0:
            print("❌ Error: No se puede calcular módulo con cero")
        else:
            resultado = num1 % num2
            print(f"{num1:.2f} % {num2:.2f} = {resultado}")
    
    elif operador == '**':
        resultado = num1 ** num2
        print(f"{num1:.2f} ** {num2:.2f} = {resultado:.2f}")
    
    else:
        print("❌ Operador no reconocido. Usa: +, -, *, /, //, %, **")
        continue
    
    # Preguntar si repetir
    repetir = input("\n¿Quieres hacer otro cálculo? (s/n): ").lower()
    if repetir != 's':
        print("¡Gracias por usar la calculadora!")
        break
    
    print()  # Línea en blanco para separar 