from typing import List, NamedTuple
from collections import namedtuple

class ProgressionItem:

    __slots__ = '__name', '__quantity'

    def __init__(self, name: str, quantity: int):
        self.__name = name
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Item quantity must be of type int, not {value.__class__.__name__}.")
        if value < 0:
            raise ValueError(f"Item quantity must be >= 0, not {value}.")
        self.__quantity = value




PROGRESSION_ITEMS: List[NamedTuple] = [
    ProgressionItem("Hylian Shield", 1),
    ProgressionItem("Progressive Sword", 4),
    ProgressionItem("Iron Boots", 1),
    ProgressionItem("Ball and Chain", 1),
    ProgressionItem("Boomerang", 1),
    ProgressionItem("Filled Bomb Bag", 3),
    ProgressionItem("Lantern", 1),
    ProgressionItem("Progressive Bow", 3),
    ProgressionItem("Progressive Clawshot", 2),
    ProgressionItem("Progressive Dominion Rod", 2),
    ProgressionItem("Progressive Fishing Rod", 2),
    ProgressionItem("Slingshot", 1),
    ProgressionItem("Spinner", 1),
    ProgressionItem("Zora Armor", 1)
]