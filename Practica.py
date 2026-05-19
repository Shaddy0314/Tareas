total_estudiantes = int(input("Ingresa el total de alumnos incritos en el colegio:  "))
asistieron_hoy = int(input("Ingresa el número de alumnos que asistieron hoy:  "))
faltaron = total_estudiantes - asistieron_hoy
porcentaje_asistencia =(asistieron_hoy / total_estudiantes) *100

es_buen_dia = porcentaje_asistencia > 90

print("\--- reporte general ---")
print(f"Total de la escuela: ´{total_estudiantes} alumnos.")
print(f"Hoy vinieron: ´{asistieron_hoy} personas.")
print(f"Faltaron a clases: ´{faltaron} estudiantes.")
print(f"Asistencia: ´{porcentaje_asistencia} %.")

if es_buen_dia and (faltaron == 0):
   print("¡Increible! asistencia perfecta.")
elif es_buen_dia:
   print("¡Casi todos vinieron! Buen trabajo. ")
else:
   print("ALERTA: hay muchos puestos vacíos hoy. ")
