from pathlib import Path


class Config:
    instance = None

    def __init__(self):
        self.NUMBER_OF_BLOBS = 500
        self.NUMBER_OF_TREES = 1000
        self.PROB_BAD_TREE = 0.5
        self.PROB_GET_EATEN = 0.5
        self.PROB_DOUBLE_REPRODUCE = 0.3
        self.ALTRUISTIC_GENE_FRACTION = 0.2
        self.STEPS = 1000
        self.GREEN_BEARD = True
        self.SIMULATION_NAME = 'green_beard_4'
        self.PLOT_PATH = Path('plots')

    def __str__(self):
        return_str = ""
        for k, v in self.__dict__.items():
            return_str += f'{k}: {v}\n'
        return return_str

    @classmethod
    def get_instance(cls):
        if not Config.instance:
            Config.instance = Config()
        return Config.instance
