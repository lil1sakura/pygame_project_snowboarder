import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Heart(pygame.sprite.Sprite):
    image = load_image("heart.png")

    def __init__(self, Skier_sprite,  x, y, hp, *group):
        super().__init__(*group)
        self.image = Heart.image
        self.hp = hp
        self.rect = self.image.get_rect()
        self.Skier_sprite = Skier_sprite
        self.rect.x = x
        self.rect.y = y



