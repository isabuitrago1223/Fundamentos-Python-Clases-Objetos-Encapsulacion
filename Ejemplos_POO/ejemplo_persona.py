class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(
            f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
        )


def main():

    persona1 = Persona("Isabella", 18)

    persona1.saludar()


if __name__ == "__main__":
    main()