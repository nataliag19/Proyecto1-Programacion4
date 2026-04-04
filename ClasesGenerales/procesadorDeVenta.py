class ProcesadorVenta:
    def __init__(self):
        self._ventas = []
        self._total = 0

    def generar_tiquete(self, comensal, plato):
        if not plato.esta_disponible():
            return None

        precio_base = plato.precio()
        precio_final = comensal.calcular_descuento(precio_base)

        plato.reducir_stock()

        venta = {
            "cliente": comensal.id_estudiante,
            "plato": plato.nombre,
            "precio": precio_final
        }

        self._ventas.append(venta)
        self._total += precio_final

        return venta

    def validar_pago(self):
        return f"Ventas hechas hasta ahora:\n{self._ventas} \n mensaje para la tesorería."
