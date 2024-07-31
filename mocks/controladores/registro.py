from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from modelos.controladores.presupuesto import ControladorDeRegistro
from modelos.presupuesto import Presupuesto, Cliente, Vendedor, Item, Formato, Calculo


class RegistroEnMemoria(ControladorDeRegistro):
    __presupuestos = []
    __clientes = []
    __vendedores = []
    __formatos = []
    __items = []

    def nuevo_presupuesto(self):
        return IPresupuesto()

    def guardar_presupuesto(self, presupuesto: IPresupuesto) -> int:
        return self.__guardar_modelo(presupuesto, self.__presupuestos)

    def guardar_cliente(self, cliente: ICliente) -> int:
        return self.__guardar_modelo(cliente, self.__clientes)

    def guardar_vendedor(self, vendedor: IVendedor) -> int:
        return self.__guardar_modelo(vendedor, self.__vendedores)

    def guardar_formato(self, formato: IFormato) -> int:
        return self.__guardar_modelo(formato, self.__formatos)

    def guardar_item(self, item: IItem) -> int:
        return self.__guardar_modelo(item, self.__items)

    @staticmethod
    def __guardar_modelo(objeto, tabla) -> int:
        if objeto.id_ is not None:
            tabla[objeto.id_] = objeto.model_dump()
        else:
            objeto.id_ = len(tabla)
            tabla.append(objeto.model_dump())
        return objeto.id_

    def leer_presupuestos(self, **params) -> list[IPresupuesto]:
        return list(self.__leer_modelos(self.__presupuestos, IPresupuesto, **params))

    def leer_vendedores(self, **params) -> list[IVendedor]:
        return list(self.__leer_modelos(self.__vendedores, IVendedor, **params))

    def leer_formatos(self, **params) -> list[IFormato]:
        return list(self.__leer_modelos(self.__formatos, IFormato, **params))

    def leer_clientes(self, **params) -> list[ICliente]:
        return list(self.__leer_modelos(self.__clientes, ICliente, **params))

    def leer_items(self, **params) -> list[IItem]:
        return list(self.__leer_modelos(self.__items, IItem, **params))

    def __leer_modelos(self, tabla, modelo, **params):
        for objeto in tabla:
            if self.__validar(objeto, params):
                yield modelo(**objeto)

    @classmethod
    def __validar(cls, objeto, params):
        if not params:
            return True
        for attrs, val in params.items():
            comparado = objeto
            for attr in attrs.split("."):
                try:
                    comparado = getattr(comparado, attr)
                except AttributeError:
                    return False
            if comparado != val:
                return False
        return True


class IVendedor(BaseModel, Vendedor):
    pass


class ICliente(BaseModel, Cliente):
    pass


class IFormato(BaseModel, Formato):
    pass


class IItem(BaseModel, Item):
    formato: IFormato


class IPresupuesto(BaseModel, Presupuesto):
    id_: int = None
    vendedor: IVendedor = None
    cliente: ICliente = None
    items: List[IItem] = Field(default_factory=list)
    total: float = 0.0


"""
class IPresupuesto(BaseModel, Presupuesto):
    id_: int
    vendedor: Vendedor
    cliente: Cliente
    items: list[IItem]
    total: Calculo


class ICliente(BaseModel, Cliente):
    id_: int


class IVendedor(BaseModel, Vendedor):
    id_: int


class IItem(BaseModel, Item):
    id_: int
    formato: Formato


class IFormato(BaseModel, Formato):
    id_: int
"""
