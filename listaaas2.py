cesta = { "manzana": 0.5, "pan": 1.2, "leche": 0.8 }

print("Introduce los artículos (escribe 'fin'o 'listo' para terminar).")

for _ in range(100):  
    articulo = input("Artículo: ")
    if articulo.lower() == "fin" or articulo.lower() == "listo":
        break
    precio = float(input("Precio: "))
    cesta[articulo] = precio

print("\nLista de compra:")
total = 0

for producto, precio in cesta.items():
    print(producto, "/", precio)
    total += precio

print("Total:", total)



