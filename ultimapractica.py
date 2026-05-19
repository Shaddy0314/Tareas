          
frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

 
lista_frase = list(frase)


contador = 0
for caracter in lista_frase:
    if caracter == letra:
        contador += 1


print(f"La letra '{letra}' aparece {contador} veces")