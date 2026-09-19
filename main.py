class Calculator:
    def __init__(self):
        self.historial: list = []

    def suma(self, a: int, b: int) -> int:
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado

    def resta(self, a: int, b: int) -> int:
        return a - b

#prueba issue david

#prueba2 con issue
""" CAMBIO NEIDER GUINDIGUA """
