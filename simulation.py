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
        trees = generate_trees()
        assign_blobs_and_trees(trees, home.get_blobs())
        for tree in trees:
            if tree.predator and len(tree.blobs) == 2:
                action_blob = tree.blobs[0]
                passive_blob = tree.blobs[1]
                if action_blob.gene == BlobGene.COWARDICE:
                    action_blob.state = BlobState.RUN_AWAY
                    passive_blob.state = BlobState.DEAD
                elif action_blob.gene == BlobGene.ALTRUISTIC:
                    action_blob.state = BlobState.SHOUT
                    passive_blob.state = BlobState.RUN_AWAY
                    p = [1 - config.PROB_GET_EATEN, config.PROB_GET_EATEN]
                    eaten = bool(np.random.choice((0, 1), size=1, p=p))
                    if eaten:
                        action_blob.state = BlobState.DEAD
                    else:
                        action_blob.state = BlobState.RUN_AWAY
            elif tree.predator and len(tree.blobs) == 1:
                tree.blobs[0].state = BlobState.RUN_AWAY

    print('hehe')


def assign_blobs_and_trees(trees, blobs):
    available_slots = trees + trees
    random.shuffle(available_slots)
    for blob in blobs:
        tree_choice = available_slots.pop()
        tree_choice.place_blob(blob)
        blob.tree = tree_choice
        blob.state = BlobState.NEAR_TREE


def generate_trees() -> list[Tree]:
    trees = []
    for tree_index in range(config.NUMBER_OF_TREES):
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
