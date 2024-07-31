from random import random

from modelos.controladores.calculo import *


class CalculadorRandom(Calculador):
    def _calculo_de_presupuesto(self, presupuesto: Presupuesto) -> Calculo:
        return Calculo(random()*1000)

    def presupuestar(self, presupuesto: Presupuesto):
        presupuesto.total = self._calculo_de_presupuesto(presupuesto)
