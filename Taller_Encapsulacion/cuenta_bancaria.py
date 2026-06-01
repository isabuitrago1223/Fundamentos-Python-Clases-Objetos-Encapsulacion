class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        """
        Constructor de la clase CuentaBancaria

        Args:
            titular (str): Nombre del titular de la cuenta
            saldo (float): Saldo inicial de la cuenta
        """
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


# Prueba de la clase CuentaBancaria
def main():

    cuenta = CuentaBancaria("Isabella Buitrago", 1000)

    print("=== Información Inicial ===")
    print("Titular:", cuenta.titular)
    print("Saldo:", cuenta.saldo)

    print("\n=== Depósito ===")
    if cuenta.depositar(500):
        print("Depósito realizado correctamente.")
    else:
        print("No fue posible realizar el depósito.")

    print("Saldo actual:", cuenta.saldo)

    print("\n=== Retiro ===")
    if cuenta.retirar(300):
        print("Retiro realizado correctamente.")
    else:
        print("No fue posible realizar el retiro.")

    print("Saldo actual:", cuenta.saldo)

    print("\n=== Intento de saldo negativo ===")
    try:
        cuenta.saldo = -100
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()