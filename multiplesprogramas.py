Estudiantes = []
niveles = ("Básico", "Intermedio", "Avanzado")

nombre = input("Nombre del estudiante: ")
nivel = input("Nivel del estudiante (Básico, Intermedio, Avanzado): ")
calificación = int(input("Calificación del estudiante: "))
materia = input("Materia del estudiante: ")

estudiante = {
    "nombre": nombre,
    "materia": materia,
    "calificacion": calificación,
    "nivel": nivel
}

Estudiantes.append(estudiante)

#Exelencia académica
if calificación >= 90:
    excelencia = "Sí"
else:
    excelencia = "No"

# Asignación de nivel
if calificación >= 90:
    nivel = niveles[2]     # Avanzado
elif calificación >= 80:
    nivel = niveles[1]     # Intermedio
else:
    nivel = niveles[0]     # Básico

    print("\n--- RESULTADOS DEL ESTUDIANTE ---")
print(f"Nombre: {nombre}")
print(f"Materia: {materia}")
print(f"Calificación: {calificación}")
print(f"Excelencia Académica: {excelencia}")
print(f"Nivel Académico: {nivel}")