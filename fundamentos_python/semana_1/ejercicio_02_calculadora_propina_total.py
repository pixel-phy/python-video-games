"""Escribe un programa que:
1. Pregunte el total de la cuenta (puede tener decimales).
2. Pregunte el porcentaje de propina que quiere dejar (10, 15, 20, o el que el usuario decida).
3. Pregunte entre cuántas personas van a dividir la cuenta.
4. Calcule:
- El monto de la propina
- El total a pagar (cuenta + propina)
- El monto por persona (total dividido entre el número de personas)
-Muestre los resultados con 2 decimales de forma clara.
-Permita repetir el cálculo hasta que el usuario escriba "salir". """

print("\n### CALCULADORA DE PROPINA ###\n")

while True:
    print("Ingrese 'salir' para cerrar: ")

    # Primera entrada:

    entrada_1 = input("Ingrese el total de la cuenta: ")
    if entrada_1.lower() == 'salir':
        print("Hasta luego!")
        break
    try:
        total_cuenta = float(entrada_1)
        if total_cuenta <= 0:
            print("El total de la cuenta debe ser mayor que cero.")
            continue
    except ValueError:
        print("Ingrese un valor adecuado para el total de la cuenta (int/float).")
        continue

    # Segunda entrada:
    
    entrada_2 = input("Ingrese el porcentaje de propina que desean aportar: ")
    if entrada_2.lower() == 'salir':
        print("Hasta luego!")
        break
    try:
        porcentaje_propina = float(entrada_2)
        if porcentaje_propina < 0:
            print("La propina debe ser mayor que cero.")
            continue
    except ValueError:
        print("Ingrese un valor porcentual adecuado para la propina (int/float).")
        continue
    # Tercera entrada:

    entrada_3 = input("Ingrese la cantidad de personas que pagarán la cuenta: ")
    if entrada_3.lower() == 'salir':
        print("Hasta luego!")
        break
    try:
        total_personas = int(entrada_3)
        if total_personas <= 0:
            print("El número de personas debe ser mayor que cero.")
    except ValueError:
        print("Ingrese una cantidad adecuada de personas (int).")
        continue
    
    # Calculo datos:
    propina = (porcentaje_propina/100) * total_cuenta
    total_pago = propina + total_cuenta
    monto_personas = total_pago/total_personas

    print(f"Cuenta: {total_cuenta:.2f}\n"
          f"Propina {porcentaje_propina}%: {propina:.2f}\n"
          f"Total a pagar: {total_pago:.2f}\n"
          f"Cada persona paga: {monto_personas:.2f}\n")