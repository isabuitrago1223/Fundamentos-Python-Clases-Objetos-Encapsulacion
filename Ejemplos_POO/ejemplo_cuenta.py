class Cuenta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):

        print(
            f"El saldo de {self.titular} es ${self.saldo}"
        )


def main():

    cuenta = Cuenta(
        "Isabella Buitrago",
        500000
    )

    cuenta.mostrar_saldo()


if __name__ == "__main__":
    main()