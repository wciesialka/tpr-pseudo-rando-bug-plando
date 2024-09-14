from random import choice
from typing import List, Dict
from copy import deepcopy
from .items import ProgressionItem

CHECKS: List[str] = [
    "Agitha Female Ant Reward",
    "Agitha Female Beetle Reward",
    "Agitha Female Butterfly Reward",
    "Agitha Female Dayfly Reward",
    "Agitha Female Dragonfly Reward",
    "Agitha Female Grasshopper Reward",
    "Agitha Female Ladybug Reward",
    "Agitha Female Mantis Reward",
    "Agitha Female Phasmid Reward",
    "Agitha Female Pill Bug Reward",
    "Agitha Female Snail Reward",
    "Agitha Female Stag Beetle Reward",
    "Agitha Male Ant Reward",
    "Agitha Male Beetle Reward",
    "Agitha Male Butterfly Reward",
    "Agitha Male Dayfly Reward",
    "Agitha Male Dragonfly Reward",
    "Agitha Male Grasshopper Reward",
    "Agitha Male Ladybug Reward",
    "Agitha Male Mantis Reward",
    "Agitha Male Phasmid Reward",
    "Agitha Male Pill Bug Reward",
    "Agitha Male Snail Reward",
    "Agitha Male Stag Beetle Reward"
]

def generate_pairings(items: List[ProgressionItem]) -> Dict[str, str]:
    '''Generate check-item pairs.

    :param items: Item listings
    :type items: List[ProgressionItem]
    :return: Check-item pairs.
    :rtype: Dict[str, ProgressionItem]
    '''
    remaining_items: List[ProgressionItem] = deepcopy(items)
    remaining_checks: List[str] = CHECKS.copy()
    pairings: Dict[str, str] = {}

    while len(remaining_checks) > 0:
        # Choose random check/item pair
        check: str = choice(remaining_checks)
        item: ProgressionItem = choice(remaining_items)
        # Remove check from pool. Remove item from the pool. If quantity isn't zero yet, add it back to the pool.
        remaining_checks.remove(check)
        remaining_items.remove(item)
        item.quantity = item.quantity - 1
        if item.quantity > 0:
            remaining_items.append(item)
        # Assign pairing
        pairings[check] = item.name
    return pairings