import random
from time import sleep
import numpy as np
import pygame
from config import Config

config = Config.get_instance()

"""
trees x:
550 - 1550

trees y:
50 - 750

tree size:
25 x 30 px

blob size:

17 x 17 px
"""


class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))


def draw_grid(screen, w_width, w_height, t, trees, home, shuffle=True):
    sleep(config.SLEEP)
    white = (255, 255, 255)
    screen.fill(white)
    blue = (0, 0, 128)

    home.image = pygame.transform.scale(home.image, (500, 800))
    screen.blit(home.image, (home.x, home.y))
    if home.get_blob_count() > 0:
        blob_positions = []
        if shuffle or t == 0:

            for x in np.linspace(50, 430, config.BLOBS_GRID_SIZE):
                for y in np.linspace(50, 730., config.BLOBS_GRID_SIZE):
                    blob_positions.append((x, y))
            random.shuffle(blob_positions)
        for blob_ctr, blob in enumerate(home.get_blobs()):
            if shuffle or t == 0:
                blob.x, blob.y = blob_positions[blob_ctr]
            screen.blit(config.IMAGES[str(blob.gene).split('.')[-1]], (blob.x, blob.y))


    tree_ctr = -1
    for x in np.linspace(550, 1500, config.TREES_GRID_SIZE):
        for y in np.linspace(50, 750., config.TREES_GRID_SIZE):
            tree_ctr += 1
            trees[tree_ctr].image = pygame.transform.scale(trees[tree_ctr].image, (25, 30))
            screen.blit(trees[tree_ctr].image, (x, y))

    else:
        tree_ctr = -1
        for x in np.linspace(550, 1500, config.TREES_GRID_SIZE):
            for y in np.linspace(50, 750., config.TREES_GRID_SIZE):
                tree_ctr += 1
                trees[tree_ctr].image = pygame.transform.scale(trees[tree_ctr].image, (25, 30))
                screen.blit(trees[tree_ctr].image, (x, y))
                if len(trees[tree_ctr].blobs) == 1:
                    blob = trees[tree_ctr].blobs[0]
                    blob.x = x - 10
                    blob.y = y + 10
                    blob.blit(screen)
                elif len(trees[tree_ctr].blobs) == 2:
                    # screen.blit(config.IMAGES[str(trees[tree_ctr].blobs[0].gene).split('.')[-1]], (x - 10, y + 15))
                    # screen.blit(config.IMAGES[str(trees[tree_ctr].blobs[1].gene).split('.')[-1]], (x + 10, y + 15))
                    blob1 = trees[tree_ctr].blobs[0]
                    blob1.x = x - 10
                    blob1.y = y + 15
                    blob2 = trees[tree_ctr].blobs[1]
                    blob2.x = x + 10
                    blob2.y = y + 15

                    blob1.blit(screen)
                    blob2.blit(screen)


    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f't = {t}', True, white, blue)
    textRect = text.get_rect()
    textRect.center = (w_width // 2, w_height + 40)
    screen.blit(text, textRect)

    pygame.display.flip()
