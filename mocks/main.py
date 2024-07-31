from mocks.calculo import CalculadorRandom
from mocks.controladores.interfaz import Interfaz
from mocks.controladores.interfaz.gui import InterfazTkinter
from mocks.controladores.registro import *
from modelos.controladores.presupuesto import ControladorDePresupuesto

registro = RegistroEnMemoria()

if __name__ == "__main__":
    print(IPresupuesto(vendedor={'id_': 0}, cliente={'id_': 0}, total=0.0))
    registro._RegistroEnMemoria__vendedores = [{'id_': 0}, {'id_': 1}]
    registro._RegistroEnMemoria__clientes = [{'id_': 0}, {'id_': 1}]
    registro._RegistroEnMemoria__formatos = [{'id_': 0}, {'id_': 1}]
    registro._RegistroEnMemoria__items = [{'id_': 0, 'formato': {'id_': 1}},
                                          {'id_': 1, 'formato': {'id_': 0}},
                                          {'id_': 2, 'formato': {'id_': 0}}]
    registro._RegistroEnMemoria__presupuestos = [{'id_': 0,
                                                  'vendedor': {'id_': 0},
                                                  'total': 2.0,
                                                  'cliente': {'id_': 0},
                                                  'items': [{'id_': 0, 'formato': {'id_': 0}},
                                                            {'id_': 1, 'formato': {'id_': 1}}]},
                                                 {'id_': 1,
                                                  'vendedor': {'id_': 0},
                                                  'total': 5.0,
                                                  'cliente': {'id_': 1},
                                                  'items': [{'id_': 2, 'formato': {'id_': 0}}]}]

    GUI = True
    if GUI:
        app = InterfazTkinter()
        controlador = ControladorDePresupuesto(registro, app, CalculadorRandom())
        app.mainloop()
    else:
        controlador = ControladorDePresupuesto(registro, Interfaz(), CalculadorRandom())
        controlador.interfaz.nuevo_presupuesto()
