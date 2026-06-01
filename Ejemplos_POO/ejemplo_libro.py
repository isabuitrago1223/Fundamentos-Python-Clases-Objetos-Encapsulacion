class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):

        print("Título:", self.titulo)
        print("Autor:", self.autor)


def main():

    libro = Libro(
        "Cien años de soledad",
        "Gabriel García Márquez"
    )

    libro.mostrar_informacion()


if __name__ == "__main__":
    main()