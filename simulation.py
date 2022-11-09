import random

import numpy as np

import config
from blob import BlobState, Blob, BlobGene
from home import Home
from tree import Tree


def simulation():
    home = Home()
    fill_home(home)
    for step in range(config.STEPS):
        shouters = 0
        print(f'\n\n\n***** DAY {step + 1} *****\n')
        print(f'Altruistic blobs: {home.get_blob_count_by_type(BlobGene.ALTRUISTIC)}')
        print(f'Cowardice blobs: {home.get_blob_count_by_type(BlobGene.COWARDICE)}')
        number_of_trees = len(home.get_blobs())//2 + 1
        trees = generate_trees(number_of_trees)
        assign_blobs_and_trees(trees, home)
        for tree in trees:
            if tree.predator and len(tree.blobs) == 2:
                action_blob = tree.blobs[0]
                passive_blob = tree.blobs[1]
                if action_blob.gene == BlobGene.COWARDICE:
                    action_blob.state = BlobState.RUN_AWAY
                    passive_blob.state = BlobState.DEAD
                elif action_blob.gene == BlobGene.ALTRUISTIC:
                    action_blob.state = BlobState.SHOUT
                    shouters += 1
                    passive_blob.state = BlobState.RUN_AWAY
                    p = [1 - config.PROB_GET_EATEN, config.PROB_GET_EATEN]
                    eaten = bool(np.random.choice((0, 1), size=1, p=p))
                    if eaten:
                        action_blob.state = BlobState.DEAD
                    else:
                        action_blob.state = BlobState.RUN_AWAY

            # if there is one blob near tree he always run away
            elif tree.predator and len(tree.blobs) == 1:
                tree.blobs[0].state = BlobState.RUN_AWAY

        print('hehe')
        for tree in trees:
            for blob in tree.blobs:
                if blob.state in [BlobState.RUN_AWAY, BlobState.NEAR_TREE]:
                    blob.state = BlobState.TO_REPRODUCE
                    home.add_blob(blob)

        new_blobs = []
        for blob in home.get_blobs():
            sons = blob.reproduce()
            for son in sons:
                new_blobs.append(son)
        home.blobs = new_blobs.copy()

    print('hehe')


def assign_blobs_and_trees(trees, home):
    blobs = home.get_blobs()
    available_slots = trees + trees
    random.shuffle(available_slots)
    for blob in blobs:
        tree_choice = available_slots.pop()
        tree_choice.place_blob(blob)
        blob.tree = tree_choice
        blob.state = BlobState.NEAR_TREE
    home.blobs = []


def generate_trees(number_of_trees=config.NUMBER_OF_TREES) -> list[Tree]:
    trees = []
    for tree_index in range(number_of_trees):
        p = [1 - config.PROB_BAD_TREE, config.PROB_BAD_TREE]
        has_predator = bool(np.random.choice((0, 1), size=1, p=p))
        trees.append(Tree(has_predator))
    return trees


def fill_home(home: Home) -> None:
    number_of_altruistic_blobs = config.NUMBER_OF_BLOBS * config.ALTRUISTIC_GENE_FRACTION
    for blob_index in range(config.NUMBER_OF_BLOBS):
        if blob_index < number_of_altruistic_blobs:
            home.add_blob(Blob(BlobGene.ALTRUISTIC))
        else:
            home.add_blob(Blob(BlobGene.COWARDICE))


simulation()
print("hehe")
