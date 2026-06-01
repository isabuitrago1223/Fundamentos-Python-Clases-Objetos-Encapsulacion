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


def registrar_prestamo():

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    if not equipos:
        print("No hay equipos registrados.")
        return

    documento = input("Documento del usuario: ")
    codigo = input("Código del equipo: ")

    usuario_encontrado = None
    equipo_encontrado = None

    for usuario in usuarios:
        if usuario.documento == documento:
            usuario_encontrado = usuario

    for equipo in equipos:
        if equipo.codigo == codigo:
            equipo_encontrado = equipo

    if usuario_encontrado is None:
        print("Usuario no encontrado.")
        return

    if equipo_encontrado is None:
        print("Equipo no encontrado.")
        return

    if equipo_encontrado.prestar():

        nuevo_prestamo = Prestamo(
            usuario_encontrado,
            equipo_encontrado
        )

        prestamos.append(nuevo_prestamo)

        print("Préstamo registrado correctamente.")

    else:
        print("El equipo no está disponible.")


def devolver_equipo():

    codigo = input("Código del equipo a devolver: ")

    for equipo in equipos:

        if equipo.codigo == codigo:

            equipo.devolver()

            print("Equipo devuelto correctamente.")
            return

    print("Equipo no encontrado.")


def ver_equipos():

    if not equipos:
        print("No hay equipos registrados.")
        return

    print("\n=== LISTA DE EQUIPOS ===")

    for equipo in equipos:
        print(equipo)


def ver_historial():

    if not prestamos:
        print("No existen préstamos registrados.")
        return

    print("\n=== HISTORIAL DE PRÉSTAMOS ===")

    for prestamo in prestamos:
        print(prestamo)


def menu():

    while True:

        print("\n===== SISTEMA DE PRÉSTAMOS =====")
        print("1. Registrar equipo")
        print("2. Registrar usuario")
        print("3. Registrar préstamo")
        print("4. Devolver equipo")
        print("5. Ver equipos")
        print("6. Ver historial")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            registrar_prestamo()

        elif opcion == "4":
            devolver_equipo()

        elif opcion == "5":
            ver_equipos()

        elif opcion == "6":
            ver_historial()

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()