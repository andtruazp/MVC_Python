from model import Cancion, CancionModel
from view import CancionVista
from controller import CancionControlador

#Instancias
cancion_m = CancionModel()
cancion_v = CancionVista()
cancion_c = CancionControlador(cancion_m, cancion_v)
while True:
    print("\nMenú:")
    print("1. Ver todas las canciones")
    print("2. Agregar nueva canción")
    print("3. Salir")

    id = 0

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        # Obtener y mostrar canciones
        cancion_c.obtenerCanciones()
    elif opcion == "2":
        # Solicitar al usuario detalles de la nueva canción
        n_id = id + 1
        n_titulo = input("Ingrese el título de la nueva canción: ")
        n_artista = input("Ingrese el nombre del artista de la nueva canción: ")
        n_genero = input("Ingrese el genero: ")

        # Crear la nueva canción
        n_cancion = Cancion(n_id, n_titulo, n_artista, n_genero)

        # Agregar la nueva canción
        cancion_c.agregarCancion(n_cancion)
        print("Canción agregada exitosamente.")
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")

