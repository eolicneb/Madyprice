from typing import List

from pydantic import BaseModel, Field


class Formato:
    id_: int


class Item:
    id_: int
    formato: Formato


class Presupuesto:
    total: float
    items: List[Item]


class IFormato(BaseModel, Formato):
    pass


class IItem(BaseModel, Item):
    formato: IFormato


class Calculo(float):
    pass


class IPresupuesto(BaseModel, Presupuesto):
    total: float = None
    items: List[IItem] = Field(default_factory=list)


if __name__ == "__main__":
    print(IPresupuesto(total=1.0,
                       items=[{'id_': 0, 'formato': {'id_': 3}},
                              {'id_': 2, 'formato': {'id_': 6}}]))
