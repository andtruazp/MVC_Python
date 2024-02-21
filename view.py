class CancionVista:
    def mostrarCanciones(self, canciones):
        print("Lista de canciones")
        for cancion in canciones:
            print(f"Título: {cancion.titulo}, Artista: {cancion.artista}, Genero: {cancion.genero}")

    def mostrarCancion(self, cancion):
        if cancion:
            print(f"Título: {cancion.titulo}, Artista: {cancion.artista}, Genero: {cancion.genero}")
        else:
            print("La canción no se encuetra")
