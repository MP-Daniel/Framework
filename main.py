class Calculator:
    def __init__(self):
        self.historial: list = []

    def suma(self, a: int, b: int) -> int:
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado

    def resta(self, a: int, b: int) -> int:
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicacion(self, a: int, b: int) -> int:
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado

    def division(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado

    def obtener_historial(self) -> list:
        return self.historial

    def limpiar_historial(self) -> None:
        self.historial = []


""" CAMBIO NEIDER GUINDIGUA """
