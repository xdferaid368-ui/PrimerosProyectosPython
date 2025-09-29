# # 
# # Ejercicio 2

# # # Crea una lista con 5 nombres de personas (los que quieras).
# # lista = ["Jose","Charo","david","Gonzalo","Hodor"]
# # # Muestra el primer nombre de la lista.
# # print(lista[0])
# # # Muestra el último nombre de la lista.
# # print(lista[4])
# # # Cambia el tercer nombre por otro distinto.
# # print(lista[2]) = "Carlos"
# # # Imprime la lista completa al final.
# # print(lista)
# # Ejercicio 3

# # # Crea una lista con 10 números enteros (los que quieras).
# # lista = [1,2,3,4,5,6,7,8,9,10]
# # # Muestra por pantalla cuántos elementos tiene la lista.
# # print(len(lista))
# # # Muestra el número más grande y el más pequeño de la lista.
# # print("el numero mas grande de la lista es",max(lista), "y el numero mas pequeño es",min(lista))
# # # Calcula la suma de todos los números de la lista.
# # print(sum(lista))
# # # Añade un número nuevo al final de la lista.
# # lista.append(11)
# # print(lista)
# # # Elimina el primer número de la lista.
# # lista.pop(0)
# # # Imprime la lista resultante al final.
# # print(lista)

# # # Ejercicio 4

# # # Crea una lista vacía para guardar nombres de frutas.
# # lista = []
# # # Pide al usuario que introduzca 5 frutas y añádelas a la lista.
# # for i in range (5):
# #     fruta=input("Introduce el nombre de una fruta: ")
# #     lista.append(fruta)
# # # Muestra la lista completa.
# # print(lista)
# # # Pregunta al usuario por el nombre de una fruta y comprueba si está en la lista.
# # # Si está, muestra en qué posición.
# # # Si no está, muestra un mensaje diciendo que no está.
# # CompFrut=input("Introduzca una Fruta a comprobar:")
# # if CompFrut in lista:
# #     print(CompFrut, "Esta en la lista")
# # # Elimina la fruta que el usuario dijo de la lista (si está).
# #     lista.remove(CompFrut)
# #     print("Se elimino", CompFrut, "De la lista")
# #     print(lista)  
# # else:
# #     print(CompFrut, "No esta en la lista") 
# #     print(lista)   
# # #Ejercicio 5

# # # Crea una lista vacía para guardar números enteros.
# # lista=[]
# # # Pide al usuario que introduzca n números (primero pregunta cuántos números quiere introducir).
# # Long = int(input("Cuantos Numeros Quieres introducir:"))
# # # Después de introducirlos todos:
# # for i in range (Long):
# #     numero = input("Introduce un numero:")
# #     lista.append(int(numero))
# # # Muestra la lista completa.
# # print(lista)
# # # Muestra los números pares y los impares por separado.
# # listapar = []
# # listaimpar=[]
# # for numero in lista:
# #     if(numero % 2 == 0):
# #         listapar.append(numero)
# #     else:
# #         listaimpar.append(numero)
# # print("los numeros pares son",listapar)
# # print("los numeros impares son", listaimpar)
# # # Muestra la suma de los números pares y la suma de los impares.
# # print("La suma de los numeros pares es",sum(listapar))
# # print("La suma de los numeros impares es",sum(listaimpar))

# # #Ejercicio 6

# # # Crea una lista vacía para guardar nombres de alumnos.
# # lista = []
# # # Pide al usuario que introduzca nombres de alumnos hasta que escriba "fin".
# # while True:
# #     nombre = input("Introduce un nombre a añadir (fin para terminar): ")
# #     if nombre.lower() == "fin":
# #         break
# #     lista.append(nombre)
# # # Después de introducir todos los nombres:
# # # Muestra la lista completa.
# # print(lista)
# # # Pide al usuario un nombre y comprueba si está en la lista:
# # nombrecomp = input("Introduzca un nombre a comprobar: ")
# # # Si está, muestra su posición.
# # if nombrecomp in lista:
# #     print("El nombre ",nombrecomp,"esta en la posicion",lista.index(nombrecomp))
# # # Si no está, muestra un mensaje diciendo que no está.
# # else:
# #     print("El nombre no esta en la lista")
# # # Pregunta al usuario un nombre para eliminarlo de la lista (si existe).
# # deleteNombre = input("Introduzca el nombre a eliminar: ")
# # if deleteNombre in lista:
# #     lista.remove(deleteNombre)
# # else:
# #     print("El nombre no esta en la lista")
# # # Muestra la lista final.
# # print(lista)

# Ejercicio 7 – Lista y estadísticas
# Crea una lista vacía para guardar edades.
lista= []
# Pide al usuario que introduzca n edades (primero pregunta cuántas).
long = int(input("Cuantas Edades quieres introducir? : "))
for i in range(long):
    edades = int(input("Introduce una edad:"))
    lista.append(edades)
# Después de introducir todas las edades:
# Muestra la lista completa.
print(lista)
# Muestra la edad más alta y la más baja.
print("La edad mas grande es ",max(lista), "y la edad mas chica es: ",min(lista))
# Calcula la media de todas las edades.
suma = sum(lista)
media = suma % long
print("la media de edad es: ", media)
# Muestra cuántas personas son mayores de 18 y cuántas son menores o iguales a 18.
listamayores = []
listamenores=[]
for edades in lista:
    if edades >= 18:
        listamayores.append(edades)
    else:
        listamenores.append(edades)
    print("Los menores tienen estos años: ", listamenores, "y los mayores tienen:", listamayores)