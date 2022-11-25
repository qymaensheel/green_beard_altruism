from blob import Blob, BlobGene
import pygame


class Home:
    def __init__(self, blobs=None, x=0, y=0):
        if blobs is None:
            blobs = []
        self.blobs = blobs
        self.x = x
        self.y = y
        self.image = pygame.image.load(r"./imgs/home.png")

    def get_blobs(self):
        return self.blobs

    def add_blob(self, blob: Blob):
        self.blobs.append(blob)

    def get_blob_count(self):
        return len(self.blobs)

    def get_blob_count_by_type(self, gene: BlobGene):
        blob_list = [blob for blob in self.get_blobs() if blob.gene == gene]
        return len(blob_list)
