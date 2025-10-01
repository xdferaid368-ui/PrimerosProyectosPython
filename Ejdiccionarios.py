# videojuegos = []
# nvideo = int(input("Numero de videojuegos a añadir: "))

# for i in range(nvideo):
#     nombre = input("Introduzca el nombre: ")
#     valoracion = int(input("Valoracion: "))
#     categoria = input("Categoria: ")

#     videojuego = {"nombre": nombre, "valoracion": valoracion, "categoria": categoria}
#     videojuegos.append(videojuego)

# # Crear listas en una sola línea
# nombres = [i["nombre"] for i in videojuegos]
# valoraciones = [i["valoracion"] for i in videojuegos]

# print("Lista de videojuegos:", (videojuegos))
# print("Lista de nombres:", (nombres))
# print("Lista de valoraciones:",(valoraciones))
# media = sum(valoraciones) / len(valoraciones)
# print("La media de las valoraciones es:", media)

asignatura1={"nombre":"servidor","profesor":"JI","horas":7}
asignatura2={"nombre":"cliente","profesor":"David","horas":5}

persona={"nombre":"David","edad":20,"esprofe":False,"asignaturas":["cliente","servidor"],"Notas":{"cliente":4.4,"servidor":2}}
persona2={"nombre":"Migue","edad":20,"esprofe":False,"asignaturas":["cliente","servidor"],"Notas":{"cliente":5,"servidor":3.4}}

alumno=[]
alumno.append(persona)
alumno.append(persona2)

for a in persona:
    suma=0
    cantidad=0
    for nota in a["Notas"].values():
        suma=suma+nota
        cantidad=cantidad+1
    media=suma/cantidad
    print("Alumno:",a["nombre"])
    print("Media:",media)
    print("Suspensos:")
    for asignatura,nota in a["Notas"].items():
        if nota<5:
            print(asignatura,nota)
# pablo = persona
# pablo["nombre"]="Pablo"
# print(persona["nombre"])
# print(pablo["nombre"])


# print(alumno[0]["asignaturas"][0]["horas"])

# asignatura1.pop("horas")
# print(asignatura1) 