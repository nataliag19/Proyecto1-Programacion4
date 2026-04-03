class ProcesadorVenta:
    def __init__(self):
        self._ventas = []
        self._total = 0

    def procesar(self, comensal, plato):
        if not plato.esta_disponible():
            return None

        precio_base = plato.precio()
        precio_final = comensal.calcular_precio_final(precio_base)

        plato.reducir_stock()

        venta = {
            "cliente": comensal.id_estudiante,
            "plato": plato.nombre,
            "precio": precio_final
        }

        self._ventas.append(venta)
        self._total += precio_final

        return venta

    def reporte(self):
        return self._ventas
