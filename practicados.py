stock = 15
total = 0

while stock > 0:
    print(f"Stock: {stock}")
    cant = int(input("¿Cuántos?: "))
    
    if cant > stock:
        print("No hay suficientes\n")
        continue
    
    precio = cant * 50
    if cant >= 3:
        precio *= 0.9
    
    stock -= cant
    total += precio
    print(f"Total: ${precio:.2f}")
    print(f"Ganado: ${total:.2f}\n")

print(f"VENTAS TOTALES: ${total:.2f}")