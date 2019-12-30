from collections import deque
from dataclasses import dataclass


@dataclass
class Unit(object):
    type: str
    pos: tuple
    attack_power: int
    enemy_type: str
    health: int = 200

    def __init__(self, pos, unit_type, attack_power=3):

        self.pos = pos
        self.type = unit_type

        types = ["E","G"]
        types.remove(self.type)

        self.enemy_type = types[0]
        self.attack_q = deque()
        self.health = 200
        if self.type == "E":
            self.attack_power = attack_power
        else:
            self.attack_power = 3


