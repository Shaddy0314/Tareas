
numeros = []
 
print("=" * 40)

print("LOTERÍA PRIMITIVA - Introduce 6 números")

print("=" * 40)
 


while len(numeros) < 6:

    try:

        n = int(input(f"Número {len(numeros) + 1} de 6 (1-49): "))

        if n < 1 or n > 49:

            print("Debe estar entre 1 y 49")

        elif n in numeros:

            print("Número ya introducido")

        else:

            numeros.append(n)

    except ValueError:

        print(" Introduce solo números")


numeros.sort()
 
print("\n" + "=" * 40)

print("RESULTADO ORDENADO:")

print(numeros)

print("=" * 40)
 