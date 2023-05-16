import json
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

    @classmethod
    def new(self,
            NUMBER_OF_BLOBS,
            NUMBER_OF_TREES,
            PROB_BAD_TREE,
            PROB_GET_EATEN,
            PROB_DOUBLE_REPRODUCE,
            ALTRUISTIC_GENE_FRACTION,
            STEPS,
            GREEN_BEARD,
            SIMULATION_NAME,
            PLOT_PATH
            ):
        config = Config.get_instance()
        config.NUMBER_OF_BLOBS = NUMBER_OF_BLOBS
        config.NUMBER_OF_TREES = NUMBER_OF_TREES
        config.PROB_BAD_TREE = PROB_BAD_TREE
        config.PROB_GET_EATEN = PROB_GET_EATEN
        config.PROB_DOUBLE_REPRODUCE = PROB_DOUBLE_REPRODUCE
        config.ALTRUISTIC_GENE_FRACTION = ALTRUISTIC_GENE_FRACTION
        config.STEPS = STEPS
        config.GREEN_BEARD = GREEN_BEARD
        config.SIMULATION_NAME = SIMULATION_NAME
        config.PLOT_PATH = Path(PLOT_PATH)
        return config

    def __str__(self):
        return_str = ""
        for k, v in self.__dict__.items():
            return_str += f'{k}: {v}\n'
        return return_str

    @classmethod
    def from_json(self, json_file):
        data = json.loads(json_file, )
        return Config.new(**data)

    @classmethod
    def get_instance(cls):
        if not Config.instance:
            Config.instance = Config()
        return Config.instance
