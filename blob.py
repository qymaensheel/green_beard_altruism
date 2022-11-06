from enum import Enum
from uuid import uuid4


class BlobGene(Enum):
    COWARDICE = 1
    ALTRUISTIC = 2


class BlobState(Enum):
    SLEEPING = 1
    NEAR_TREE = 2
    SHOUT = 3
    RUN_AWAY = 4
    DEAD = 5
    TO_REPRODUCE = 6


class Blob:
    def __init__(self, gene: BlobGene):
        self.id = uuid4()
        self.gene = gene
        self.state = BlobState.SLEEPING
        self.tree = None


    def reproduce(self):
        pass

    def __str__(self):
        return f'Blob {self.id}, gene: {self.gene}, state: {self.state}'
