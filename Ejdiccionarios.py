videojuegos = []
nvideo = int(input("Numero de videojuegos a añadir: "))

for i in range(nvideo):
    nombre = input("Introduzca el nombre: ")
    valoracion = int(input("Valoracion: "))
    categoria = input("Categoria: ")

    videojuego = {"nombre": nombre, "valoracion": valoracion, "categoria": categoria}
    videojuegos.append(videojuego)

# Crear listas en una sola línea
nombres = [v["nombre"] for v in videojuegos]
valoraciones = [v["valoracion"] for v in videojuegos]

print("Lista de videojuegos (diccionarios):")
print(videojuegos)

print("Lista de nombres:")
print(nombres)

print("Lista de valoraciones:")
print(valoraciones)

# Media usando directamente la lista de valoraciones
media = sum(valoraciones) / len(valoraciones)
print("La media de las valoraciones es:", media)
