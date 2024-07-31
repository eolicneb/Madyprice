from __future__ import annotations

from modelos.controladores.calculo import Calculador, ErrorDePresupuesto
from modelos.presupuesto import Presupuesto, Cliente, Vendedor, Item, Formato


class ControladorDePresupuesto:
    registrador: ControladorDeRegistro
    interfaz: ControladorDeInterfaz
    calculador: Calculador

    def __init__(self, registrador, interfaz, calculador):
        self.registrador = registrador
        self.interfaz = interfaz
        self.calculador = calculador

        self.interfaz.controlador = self

    def nuevo_presupuesto(self):
        presupuesto = self.registrador.nuevo_presupuesto()
        presupuesto.cliente = self.interfaz.pedir_cliente()
        presupuesto.vendedor = self.interfaz.pedir_vendedor()
        presupuesto.items = self.interfaz.pedir_items()
        try:
            self.calculador.presupuestar(presupuesto)
            presupuesto.id_ = self.registrador.guardar_presupuesto(presupuesto)
            self.interfaz.mostrar_presupuesto(presupuesto)
        except ErrorDePresupuesto as error:
            self.interfaz.mostrar_error_de_presupuesto(error)

    def lista_de_clientes(self, *args) -> list[Cliente]:
        return self.registrador.leer_clientes(*args)

    def lista_de_vendedores(self, *args) -> list[Vendedor]:
        return self.registrador.leer_vendedores(*args)

    def lista_de_formatos(self, *args) -> list[Formato]:
        return self.registrador.leer_formatos(*args)

    def lista_de_items(self, *args) -> list[Item]:
        return self.registrador.leer_items(*args)


class ControladorDeRegistro:
    def guardar_presupuesto(self, presupuesto) -> int:
        pass

    def leer_clientes(self, param) -> list[Cliente]:
        pass

    def leer_vendedores(self, param) -> list[Vendedor]:
        pass

    def leer_formatos(self, param) -> list[Formato]:
        pass

    def leer_items(self, param) -> list[Item]:
        pass

    def nuevo_presupuesto(self) -> Presupuesto:
        pass


class ControladorDeInterfaz:
    controlador: ControladorDePresupuesto

    def pedir_cliente(self) -> Cliente:
        pass

    def pedir_vendedor(self) -> Vendedor:
        pass

    def pedir_items(self) -> list[Item]:
        pass

    def mostrar_presupuesto(self, presupuesto: Presupuesto):
        pass

    def mostrar_error_de_presupuesto(self, error: ErrorDePresupuesto):
        pass
