class Usuario:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} - {self.documento}"