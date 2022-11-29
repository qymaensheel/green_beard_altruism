import pygame


class Config:
    instance = None

    def __init__(self):
        self.NUMBER_OF_BLOBS = 50
        self.NUMBER_OF_TREES = 225
        self.PROB_BAD_TREE = 0.6
        self.PROB_GET_EATEN = 0.5
        self.PROB_DOUBLE_REPRODUCE = 0.3
        self.ALTRUISTIC_GENE_FRACTION = 0.5
        self.STEPS = 200
        self.GREEN_BEARD = True
        self.TREES_GRID_SIZE = 15
        self.BLOBS_GRID_SIZE = 20
        self.SLEEP = 2
        self.AUTORUN = True
        self.BLOB_ANNOTATION_SIZE = (25, 25)

        self.IMAGES = {
            "ALTRUISTIC": pygame.transform.scale(pygame.image.load('./imgs/blob_altruistic.png'), (17, 17)),
            "COWARDICE": pygame.transform.scale(pygame.image.load('./imgs/blob_coward.png'), (17, 17)),
            "SHOUT": pygame.transform.scale(pygame.image.load('./imgs/shouting.png'), self.BLOB_ANNOTATION_SIZE),
            "DEAD": pygame.transform.scale(pygame.image.load('./imgs/rip_blob.png'), self.BLOB_ANNOTATION_SIZE),
            "RUN_AWAY": pygame.transform.scale(pygame.image.load('./imgs/omg.png'), self.BLOB_ANNOTATION_SIZE)
        }



    def __str__(self):
        return_str = ""
        for k, v in self.__dict__.items():
            if k != 'IMAGES':
                return_str += f'{k}: {v}\n'

        return return_str

    @classmethod
    def get_instance(cls):
        if not Config.instance:
            Config.instance = Config()
        return Config.instance
