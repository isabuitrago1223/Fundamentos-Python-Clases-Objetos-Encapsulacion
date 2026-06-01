from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo

equipos = []
usuarios = []
prestamos = []


def registrar_equipo():
    codigo = input("Código del equipo: ")
    nombre = input("Nombre del equipo: ")

    equipos.append(Equipo(codigo, nombre))

    print("Equipo registrado correctamente.")


def registrar_usuario():
    documento = input("Documento: ")
    nombre = input("Nombre: ")

    usuarios.append(Usuario(documento, nombre))

    print("Usuario registrado correctamente.")


def ver_equipos():
    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        print(equipo)


def menu():

    while True:

        print("\n===== SISTEMA DE PRÉSTAMOS =====")
        print("1. Registrar equipo")
        print("2. Registrar usuario")
        print("3. Ver equipos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            ver_equipos()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()