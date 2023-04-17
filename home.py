from blob import Blob, BlobGene


class Home:
    def __init__(self, blobs=None):
        if blobs is None:
            blobs = []
        self.blobs = blobs

    def get_blobs(self):
        return self.blobs

    def add_blob(self, blob: Blob):
        self.blobs.append(blob)

    def get_blob_count(self):
        return len(self.blobs)

    def get_blob_count_by_type(self, gene: BlobGene):
        blob_list = [blob for blob in self.get_blobs() if blob.gene == gene]
        return len(blob_list)
