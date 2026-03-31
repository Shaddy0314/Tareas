print("Registro de los estudiantes para el gran evento")
print("Escribe 'fin' para terminar el registro\n")

# Lista 
estudiantes = []

# Diccionario
tareas_por_habilidad = {
    "diseño": "Decoración del evento",
    "programación": "Sistema de registro digital",
    "marketing": "Promoción y redes sociales",
    "cálculos": "Finanzas y presupuesto",
    "decoración": "Ambientación del salón",
    "logística": "Coordinación de actividades",
    "fotografía": "Cobertura fotográfica del evento",
    "música": "Ambientación musical",
    "cocina": "Preparación de alimentos",
    "atención al cliente": "Recepción y atención a los asistentes",
    "Administración": "Gestión de recursos y voluntarios",
    "Redes sociales": "Promoción y difusión del evento",
    "Organización": "Planificación y coordinación general"
}

# Estudiantes ingresan su información
for _ in range(100):
    nombre = input("Nombre del estudiante: ")
    if nombre.lower() == "fin":
        break

    habilidad = input("Habilidad del estudiante: ")
    horas = int(input("Horas disponibles: "))

    estudiante = (nombre, habilidad, horas)
    estudiantes.append(estudiante)

# Orden de los estudiantes registrados
print("\n--- Estudiantes registrados y tareas asignadas ---")
total_horas = 0

for nombre, habilidad, horas in estudiantes:

    tarea = tareas_por_habilidad.get(habilidad.lower(), "Apoyo general")

    print(f"{nombre} / {habilidad} / {horas} horas / Tarea: {tarea}")

    total_horas += horas

# Estudiantes registrados
cantidad_estudiantes = len(estudiantes)

print("\nTotal de horas donadas:", total_horas)
print("Cantidad de estudiantes registrados:", cantidad_estudiantes)
