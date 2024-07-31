from __future__ import annotations


class Calculo(float):
    pass


class Presupuesto:
    id_: int
    vendedor: Vendedor
    cliente: Cliente
    items: list[Item]
    total: float


class Vendedor:
    id_: int


class Cliente:
    id_: int


class Item:
    id_: int
    formato: Formato


class Formato:
    id_: int

