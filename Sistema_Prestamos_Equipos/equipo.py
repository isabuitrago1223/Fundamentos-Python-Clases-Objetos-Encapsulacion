class Equipo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.__disponible = True

    @property
    def disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"{self.codigo} - {self.nombre} ({estado})"