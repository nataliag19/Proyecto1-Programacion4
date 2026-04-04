from ClasesGenerales.procesadorDeVenta import ProcesadorVenta
from ClasesGenerales.menuDelDia import MenuDia
from ClasesGenerales.plato import Plato
from ClasesGenerales.comensal import Comensal

class SistemaNutriUTP:
    def __init__(self):
        self.menu = None
        self.procesador = ProcesadorVenta()

    def crear_menu(self):
        fecha = input("Fecha del menú: ")
        self.menu = MenuDia(fecha)

        cantidad_platos_a_ingresar = int(input("Cantidad de platos: "))
        for _ in range(cantidad_platos_a_ingresar):
            nombre_plato = input("Nombre del plato: ")
            precio_plato = float(input("Precio del plato: "))
            plato_veg = input("Es un plato vegetariano (si/no): ").lower() == "si"
            cantidad_plato = int(input("Cantidad disponible de este plato: "))

            self.menu.agregar_plato(Plato(nombre_plato, precio_plato, plato_veg, cantidad_plato))

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

                while True:
                    preferencia = int(input("Ingrese su preferencia:\n 1. Estándar\n 2.Vegetariano\n"))
                    if preferencia == 1 or preferencia == 2:
                        break
                    else:
                        print("Ingrese una opción válida.\n")

                print("Lista de platos:\n")
                platos = self.menu.seleccionar_opcion(preferencia - 1)
                id_plato = int(input("Seleccione su plato: ")) - 1
                plato = platos[f"{id_plato}"]

                if not plato:
                    print("❌ Opción inválida")
                    continue

                venta = self.procesador.generar_tiquete(comensal, plato)

                if venta:
                    print(f"✔️ Compra realizada: {venta}")
                else:
                    print("❌ Plato agotado")

            elif op == "2":
                ventas = self.procesador.reporte()
                print("\n=== REPORTE ===")
                for venta in ventas:
                    print(f"{venta['cliente']} -> {venta['plato']} (${venta['precio']})")
                print(f"\nTOTAL: ${self.procesador._total}")

            elif op == "3":
                print("Saliendo...")
                break

            else:
                print("❌ Opción inválida")
