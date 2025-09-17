import datetime

# Obtener la fecha y hora actual
hoy = datetime.datetime.now()

# Mostrar la fecha completa
print("Hoy es:", hoy)

# Mostrar solo el día de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Hoy es:", dias_semana[hoy.weekday()])

# Mostrar solo la fecha (sin hora)
print("Fecha de hoy:", hoy.date())
