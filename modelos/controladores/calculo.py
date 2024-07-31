from modelos.presupuesto import Presupuesto, Calculo


class ErrorDePresupuesto(Exception):
    pass


class Calculador:
    def presupuestar(self, presupuesto: Presupuesto):
        pass

    def _calculo_de_presupuesto(self, presupuesto: Presupuesto) -> Calculo:
        pass
