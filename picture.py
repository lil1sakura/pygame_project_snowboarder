import os
import sys
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Opisanie(pygame.sprite.Sprite):
    image = load_image("opisanie.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Opisanie.image
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 530


class Krest(pygame.sprite.Sprite):
    image = load_image("krest.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Krest.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 20


class Play_music(pygame.sprite.Sprite):
    image = load_image("turn on music.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Play_music.image
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 530


class Stop_music(pygame.sprite.Sprite):
    image = load_image("turn off music.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Stop_music.image
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 530