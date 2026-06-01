from datetime import datetime


class Prestamo:
    def __init__(self, usuario, equipo):
        self.usuario = usuario
        self.equipo = equipo
        self.fecha = datetime.now()

    def __str__(self):
        return (
            f"Usuario: {self.usuario.nombre} | "
            f"Equipo: {self.equipo.nombre} | "
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )