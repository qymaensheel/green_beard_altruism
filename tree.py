from uuid import uuid4

from blob import Blob


class Tree:
    def __init__(self, predator: bool):
        self.id = uuid4()
        self.predator = predator
        self.blobs = []

    def place_blob(self, blob: Blob):
        if len(self.blobs) < 2:
            self.blobs.append(blob)
            blob.tree = self
        else:
            raise ValueError('Tree is full')
