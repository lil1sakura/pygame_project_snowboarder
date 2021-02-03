import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tree(pygame.sprite.Sprite):
    image = load_image("Tree.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Tree.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(300, 1500)
        self.rect.y = random.randrange(1080, 1081)

    def update(self):
        self.rect.y -= 3


