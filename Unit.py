from collections import deque
from dataclasses import dataclass


@dataclass
class Unit:
    type: str
    pos: tuple
    apower: int
    health: int = 200

    def __post_init__(self):

        types = ["E","G"]
        types.remove(self.type)

        self.enemy_type = types[0]
        self.attack_q = deque()
        self.health = 200
        if self.type == "E":
            self.attack_power = self.apower
        else:
            self.attack_power = 3


