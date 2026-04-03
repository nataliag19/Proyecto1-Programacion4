class Comensal:
    def __init__(self, id_estudiante, tipo_subsidio):
        self.id_estudiante = id_estudiante
        self.tipo_subsidio = tipo_subsidio

    def calcular_precio_final(self, precio):
        if self.tipo_subsidio == "alto":
            return precio * 0.5
        elif self.tipo_subsidio == "medio":
            return precio * 0.7
        elif self.tipo_subsidio == "bajo":
            return precio * 0.9
        return precio
