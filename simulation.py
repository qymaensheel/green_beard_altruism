import random

import numpy as np
from matplotlib import pyplot as plt

from blob import BlobState, Blob, BlobGene
from config import Config
from home import Home
from statistics import Statistics, Day
from tree import Tree


def simulation(config=Config.get_instance(), uuid=-1):
    print(config)
    print(uuid)
    statistics = Statistics()
    home = Home()
    fill_home(home, config)
    step = -1
    while step <= config.STEPS:
        step += 1
        trees = generate_trees(config)
        altruistic_population = home.get_blob_count_by_type(BlobGene.ALTRUISTIC)
        cowardice_population = home.get_blob_count_by_type(BlobGene.COWARDICE)
        statistics.days.append(Day(altruistic_population, cowardice_population))
        assign_blobs_and_trees(trees, home)

        print(f'\n***** DAY {step + 1} *****\n')
        print(f'Altruistic blobs: {altruistic_population}')
        print(f'Cowardice blobs: {cowardice_population}')

        shouters = 0
        for tree in trees:
            if tree.predator and len(tree.blobs) == 2:
                action_blob = tree.blobs[0]
                passive_blob = tree.blobs[1]
                if config.GREEN_BEARD:
                    action = action_blob.gene == BlobGene.ALTRUISTIC and passive_blob.gene == BlobGene.ALTRUISTIC
                else:
                    action = action_blob.gene == BlobGene.ALTRUISTIC
                if action_blob.gene == BlobGene.COWARDICE:
                    action_blob.state = BlobState.RUN_AWAY
                    passive_blob.state = BlobState.DEAD
                elif action:
                    action_blob.state = BlobState.SHOUT
                    shouters += 1
                    passive_blob.state = BlobState.RUN_AWAY
                else:
                    action_blob.state = BlobState.RUN_AWAY
                    passive_blob.state = BlobState.DEAD
            # if there is one blob near tree he always run away
            elif tree.predator and len(tree.blobs) == 1:
                tree.blobs[0].state = BlobState.RUN_AWAY

        for tree in trees:
            if tree.predator and len(tree.blobs) == 2 and tree.blobs[0].state == BlobState.SHOUT:
                action_blob = tree.blobs[0]
                p = [1 - config.PROB_GET_EATEN, config.PROB_GET_EATEN]
                eaten = bool(np.random.choice((0, 1), size=1, p=p))
                if eaten:
                    action_blob.state = BlobState.DEAD
                else:
                    action_blob.state = BlobState.RUN_AWAY
        # ACTIONS (DEAD, SHOUTING ETC)
        for tree in trees:
            for blob in tree.blobs:
                if blob.state in [BlobState.RUN_AWAY, BlobState.NEAR_TREE]:
                    blob.state = BlobState.TO_REPRODUCE
                    home.add_blob(blob)
            tree.blobs = []

        new_blobs = []
        for blob in home.get_blobs():
            sons = blob.reproduce()
            for son in sons:
                new_blobs.append(son)
        home.blobs = new_blobs.copy()

    save_txt_file(config, str(uuid))
    plot(statistics, str(config.PLOT_PATH / str(uuid)))


def plot(statistics, plot_path):
    fig, ax = plt.subplots(figsize=[10, 5])
    ax.plot(list(map(lambda day: day.altruistic_population, statistics.days)), color='g', label='green beard')
    ax.plot(list(map(lambda day: day.cowardice_population, statistics.days)), color='y', label='cowardice')
    ax.legend()
    ax.set_xlabel('Days')
    ax.set_ylabel('Population')
    title = ax.set_title('Population change')
    fig.tight_layout()
    title.set_y(1.05)
    fig.savefig(plot_path)


def save_txt_file(config, uuid) -> None:
    with open((config.PLOT_PATH / f'{uuid}.txt'), 'w') as f:
        f.write(str(config))


def assign_blobs_and_trees(trees, home):
    blobs = home.get_blobs()
    available_slots = trees + trees
    random.shuffle(available_slots)
    for blob in blobs:
        if len(available_slots) > 0:
            tree_choice = available_slots.pop()
            tree_choice.place_blob(blob)
            blob.tree = tree_choice
            blob.state = BlobState.NEAR_TREE
    home.blobs = []


def generate_trees(config) -> list[Tree]:
    number_of_trees = config.NUMBER_OF_TREES
    trees = []
    for tree_index in range(number_of_trees):
        p = [1 - config.PROB_BAD_TREE, config.PROB_BAD_TREE]
        has_predator = bool(np.random.choice((0, 1), size=1, p=p))
        trees.append(Tree(has_predator))
    return trees


def fill_home(home: Home, config) -> None:
    number_of_altruistic_blobs = config.NUMBER_OF_BLOBS * config.ALTRUISTIC_GENE_FRACTION
    for blob_index in range(config.NUMBER_OF_BLOBS):
        if blob_index < number_of_altruistic_blobs:
            home.add_blob(Blob(BlobGene.ALTRUISTIC))
        else:
            home.add_blob(Blob(BlobGene.COWARDICE))


if __name__ == '__main__':
    simulation()
