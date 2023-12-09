class Cajero:

    def saldoActual(self, sa):
        return sa

    def deposito(self, dep, sa):
        return dep + sa

cajero = Cajero()  # Crear una instancia de la clase Cajero

saldo = 10000  # Establecer un saldo inicial

while True:
    print("1. Consultar saldo")
    print("2. Realizar depósito")
    print("3. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        print("Saldo actual:", cajero.saldoActual(saldo))
    elif opcion == 2:
        monto_deposito = float(input("Ingrese el monto a depositar: "))
        saldo = cajero.deposito(monto_deposito, saldo)
        print("Depósito realizado. Saldo actual:", saldo)
    elif opcion == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")


