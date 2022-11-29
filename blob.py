import random
from enum import Enum
from uuid import uuid4

import pygame

from config import Config

config = Config.get_instance()


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
        self.x = None
        self.y = None

    def reproduce(self):
        if random.random() < config.PROB_DOUBLE_REPRODUCE:
            son = Blob(self.gene)
            return [son]
        else:
            son1 = Blob(self.gene)
            son2 = Blob(self.gene)
            return [son1, son2]

    def blit(self, screen: pygame.display):
        screen.blit(config.IMAGES[str(self.gene).split('.')[-1]], (self.x, self.y))
        annotation_position = (self.x - 5, self.y - 20)
        match self.state:
            case BlobState.DEAD:
                screen.blit(config.IMAGES['DEAD'], annotation_position)
            case BlobState.SHOUT:
                screen.blit(config.IMAGES['SHOUT'], annotation_position)
            case BlobState.RUN_AWAY:
                screen.blit(config.IMAGES['RUN_AWAY'], annotation_position)

    def __str__(self):
        return f'Blob {self.id}, gene: {self.gene}, state: {self.state}'
