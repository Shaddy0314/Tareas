# Cajero automático simple
saldo = 5000
limite = 1000

print("=== CAJERO ===")
print(f"Saldo: ${saldo}")

while True:
    monto = float(input("\n¿Cuánto retirar? (0=salir): $"))
    if monto == 0:
        print("Adiós")
        break
    elif monto < 0:
        print("Monto inválido")
    elif monto > limite:
        print(f"Límite: ${limite}")
    elif monto > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= monto
        print(f"Retiraste ${monto}")
        print(f"Nuevo saldo: ${saldo}")
        
        if saldo == 0:
            print("Sin saldo")     
            break
