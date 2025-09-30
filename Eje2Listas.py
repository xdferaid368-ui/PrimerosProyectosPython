# Una tienda de videojuegos quiere llevar un registro de las valoraciones que los clientes otorgan a sus productos.
# Escribe un programa en Python que:
# Disponga de una lista inicial con varios nombres de videojuegos (por ejemplo: ["Zelda", "FIFA", "Minecraft", "Call of Duty", "Animal Crossing"]).
listvideojuegos = ["Zelda", "FIFA", "Minecraft", "Call of Duty", "Animal Crossing"]
listvalora = []

for juego in listvideojuegos:
    while True:
        try:
            valoracion = int(input(f"Introduzca una valoración del 1 al 10 para el videojuego '{juego}': "))
            if 1 <= valoracion <= 10:
                listvalora.append(valoracion)
                break
            # Si el usuario introduce un número fuera de ese rango, deberá mostrarse un mensaje de advertencia y volver a solicitarse la valoración.
            else:
                print("debe ser un numero entre 1 y 10")
        except ValueError:
            print("No valido")

# Al finalizar, el programa debe:
# Mostrar todas las valoraciones recogidas junto al nombre de cada videojuego.
for i in range(len(listvideojuegos)):
    print("El videojuego", listvideojuegos[i], "tiene una valoración de", listvalora[i])
print(listvalora)
# Calcular y mostrar la media de todas las valoraciones.
suma = sum(listvalora)
media = suma%5
# Indicar cuántos juegos han recibido una valoración mayor o igual a 8.
listmayor8 = []
for valoracion in listvalora:
    if valoracion >= 8:
        listmayor8.append(valoracion)
        print("Los juegos con valoracion mayor a 8 son", listmayor8)
# Mostrar el videojuego con la mejor valoración y el que tenga la peor.
# listvalora.sort
# for i in range(len(listvalora)):
#     #ESTO ESTA MAL!!!
#     print("El videojuego con mas valoracion es el videojuego"),listvideojuegos[i]," con una valoracion de", listvalora[4]
#     print("El videojuego con mas valoracion es el videojuego"),listvideojuegos[i]," con una valoracion de", listvalora[1]
# # Si por algún motivo no se han podido registrar valoraciones válidas, el programa deberá mostrar un mensaje indicando que no hay datos para analizar.
#     #ESTO ESTA MAL!!!
# if(ValueError):
#     print("NO HAY DATOS PARA ANALIZAR")

