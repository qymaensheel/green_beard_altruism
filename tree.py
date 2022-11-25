from uuid import uuid4
from blob import Blob
import pygame


class Tree:
    def __init__(self, predator: bool):
        self.id = uuid4()
        self.predator = predator
        self.blobs = []
        if self.predator:
            self.image = pygame.image.load(r"./imgs/predator_tree.png")
        else:
            self.image = pygame.image.load(r"./imgs/tree.png")

    def place_blob(self, blob: Blob):
        if len(self.blobs) < 2:
            self.blobs.append(blob)
            blob.tree = self
        else:
            raise ValueError('Tree is full')
