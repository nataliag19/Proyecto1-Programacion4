class MenuDia:
    def __init__(self, fecha):
        self.fecha = fecha
        self._platos = []

    def agregar_plato(self, plato):
        self._platos.append(plato)

    def mostrar(self):
        print(f"\n=== MENÚ ({self.fecha}) ===")
        for i, p in enumerate(self._platos):
            print(f"{i+1}. {p.descripcion()}")

    def obtener(self, indice):
        if 0 <= indice < len(self._platos):
            return self._platos[indice]
        return None
