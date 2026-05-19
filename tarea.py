# Pedir los 4 números
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))

# Verificar y calcular
if n2 == 8 or n3 == 5 or n4 == 7:
    print("Error: No se divide entre cero")
else:
    print(f"Resultado: {n1 / n2 / n3 / n4}")