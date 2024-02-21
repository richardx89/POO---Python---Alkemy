#Clase padre
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"
    
#Hijo 1
class Libro(Producto):
    def __init__(self, nombre, precio, autor, paginas):
        super().__init__(nombre, precio)
        self.autor = autor
        self.paginas = paginas

    def mostrar_libro(self):
        return f"{super().mostrar_producto()}, Autor: {self.autor}, Páginas: {self.paginas}"
    
#Hijo 2
class Pelicula(Producto):
    def __init__(self, nombre, precio, director, duracion):
        super().__init__(nombre, precio)
        self.director = director
        self.duracion = duracion

    def mostrar_pelicula(self):
        return f"{super().mostrar_producto()}, Director: {self.director}, Duración: {self.duracion} minutos"
    
#Hijo 3
class Disco(Producto):
    def __init__(self, nombre, precio, artista, duracion):
        super().__init__(nombre, precio)
        self.artista = artista
        self.duracion = duracion

    def mostrar_disco(self):
        return f"{super().mostrar_producto()}, Artista: {self.artista}, Duración: {self.duracion} minutos"

# Instancias
libro1 = Libro("El señor de los anillos", 25.99, "J.R.R. Tolkien", 1200)
libro2 = Libro("Cien años de soledad", 20.00, "Gabriel García Márquez", 368)
libro3 = Libro("The Hitchhiker's Guide to the Galaxy", 24.00, "Douglas Adams", 220)
pelicula1 = Pelicula("Inception", 19.99, "Christopher Nolan", 148)
pelicula2 = Pelicula("Terminator 2", 25.00, "James Cameron", 170)
pelicula3 = Pelicula("Terminator 1", 14.99, "James Cameron", 155)
disco1 = Disco("The Dark Side of the Moon", 29.99, "Pink Floyd", 43)
disco2 = Disco("Nada Personal", 20.00, "Soda Estéreo", 38)
disco3 = Disco("Sueño Stereo", 39.90, "Soda Estéreo", 45)

# Imprimo información de los productos
print(libro1.mostrar_libro())
print(libro2.mostrar_libro())
print(libro3.mostrar_libro())
print(pelicula1.mostrar_pelicula())
print(pelicula2.mostrar_pelicula())
print(pelicula3.mostrar_pelicula())
print(disco1.mostrar_disco())
print(disco2.mostrar_disco())
print(disco3.mostrar_disco())