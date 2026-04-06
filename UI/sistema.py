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

        cantidad_platos_a_ingresar = input("\nCantidad de platos: ")

        if cantidad_platos_a_ingresar.isdigit():
            cantidad_platos_a_ingresar = int(cantidad_platos_a_ingresar)
        else:
            cantidad_platos_a_ingresar = 0 

        if cantidad_platos_a_ingresar <= 0:
            cantidad_platos_a_ingresar = 1
        
        for _ in range(cantidad_platos_a_ingresar):
            nombre_plato = input("\nNombre del plato: ")
            precio_plato = input("Precio del plato: ")
            try:
                precio_plato = float(precio_plato)
            except ValueError:
                precio_plato = 1000.0
            
            plato_veg = input("Es un plato vegetariano (si/no): ").lower() == "si"
            cantidad_plato = input("Cantidad disponible de este plato: ")
            try:
                cantidad_plato = int(cantidad_plato)
            except ValueError:
                cantidad_plato = 1
            
            dic_plato = {'nombre': nombre_plato, 'precio': precio_plato, 'plato_veg':plato_veg, 'cantidad':cantidad_plato}

            self.menu.agregar_plato(Plato(dic_plato))

    def registrar_comensal(self):
        tipo = input("\nSubsidio (alto/medio/bajo/ninguno): ")
        return Comensal(tipo)

    def ejecutar(self):
        self.crear_menu()

        while True:
            print("\n1. Comprar plato")
            print("2. Ver reporte")
            print("3. Salir")

            op = input("\nOpción: ")

            if op == "1":
                comensal = self.registrar_comensal()

                while True:
                    preferencia = input("\nIngrese su preferencia:\n 1. Estándar\n 2.Vegetariano\n")
                    if preferencia == '1' or preferencia == '2':
                        break
                    else:
                        print("Ingrese una opción válida.\n")
                preferencia = int(preferencia)
                print("Lista de platos:\n")
                platos = self.menu.seleccionar_opcion(preferencia)
                for id_mostrar, objeto_plato in platos.items():
                    print(f"{id_mostrar}. {objeto_plato.descripcion_detallada()}")
                
                if not platos:
                    print("❌ No hay platos disponibles para esta preferencia.")
                else:

                    try:
                        id_plato = int(input("\nSeleccione su plato: "))
                    except ValueError:
                        id_plato = 0
                
                try:
                    plato = platos.get(f"{id_plato}")
                
                    venta = self.procesador.generar_tiquete(comensal, plato)

                    if venta:
                        print(f"\n✔️ Compra realizada: {venta}")
                    else:
                        print("\n❌ Plato agotado")
                except:
                    print("\n❌ Plato no existente")
            elif op == "2":
                ventas = self.procesador.validar_pago()
                print("\n=== REPORTE ===\n")
                for venta in ventas:
                    print(f"{venta['cliente']} -> {venta['plato']} (${venta['precio']})")
                print(f"\nTOTAL: ${self.procesador._total}")

            elif op == "3":
                print("\nSaliendo...")
                break

            else:
                print("\n❌ Opción inválida")

