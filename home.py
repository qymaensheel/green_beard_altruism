from blob import Blob, BlobState


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
