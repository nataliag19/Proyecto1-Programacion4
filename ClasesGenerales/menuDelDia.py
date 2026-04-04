class MenuDia:
    def __init__(self, fecha):
        self.fecha = fecha
        self._opciones = []

    def agregar_plato(self, plato):
        self._opciones.append(plato)

    def mostrar(self):
        print(f"\n=== MENÚ ({self.fecha}) ===")
        for iterador, plato in enumerate(self._opciones):
            print(f"{iterador+1}. {plato.descripcion_detallada()}")

    def seleccionar_opcion(self, tipo_preferencia):
        return self._aislar_seleccion(tipo_preferencia)
    
    def _aislar_seleccion(self, tipo_preferencia):
        es_veg = (tipo_preferencia == 2)
        platos_filtrados = [plato for plato in self._opciones if plato.es_vegetariano == es_veg]
        return {str(i+1): plato for i, plato in enumerate(platos_filtrados)}