class SistemaNutriUTP:
    def __init__(self):
        self.menu = None
        self.procesador = ProcesadorVenta()

    def crear_menu(self):
        fecha = input("Fecha del menú: ")
        self.menu = MenuDia(fecha)

        n = int(input("Cantidad de platos: "))
        for _ in range(n):
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            veg = input("Vegetariano (si/no): ").lower() == "si"
            cantidad = int(input("Cantidad disponible: "))

            self.menu.agregar_plato(Plato(nombre, precio, veg, cantidad))

    def registrar_comensal(self):
        id_est = input("ID estudiante: ")
        tipo = input("Subsidio (alto/medio/bajo/ninguno): ")
        return Comensal(id_est, tipo)

    def ejecutar(self):
        self.crear_menu()

        while True:
            print("\n1. Comprar plato")
            print("2. Ver reporte")
            print("3. Salir")

            op = input("Opción: ")

            if op == "1":
                comensal = self.registrar_comensal()
                self.menu.mostrar()

                idx = int(input("Seleccione plato: ")) - 1
                plato = self.menu.obtener(idx)

                if not plato:
                    print("❌ Opción inválida")
                    continue

                venta = self.procesador.procesar(comensal, plato)

                if venta:
                    print(f"✔️ Compra realizada: {venta}")
                else:
                    print("❌ Plato agotado")

            elif op == "2":
                self.procesador.reporte()

            elif op == "3":
                print("Saliendo...")
                break

            else:
                print("❌ Opción inválida")
