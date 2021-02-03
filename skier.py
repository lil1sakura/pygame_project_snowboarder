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


class Skier(pygame.sprite.Sprite):
    image = load_image("sk.png")

    def __init__(self, Skier_sprite, fridge_boarder, *group):
        super().__init__(*group)
        self.image = Skier.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 500
        self.flag_running = True
        self.flag_skier_transform = True
        self.Skier_sprite = Skier_sprite
        self.fridge_boarder = fridge_boarder
        self.hp = 2
        self.point = 0

    def update(self):
        self.rect.y -= 3
        self.speedx = 0
        self.speedy = 0

        if pygame.sprite.collide_mask(self, self.fridge_boarder[0]):
            self.rect.y = 425
            self.rect.x = 847
            self.hp -= 1

        if pygame.sprite.collide_mask(self, self.fridge_boarder[1]):
            self.rect.y = 425
            self.rect.x = 847
            self.hp -= 1

        if pygame.sprite.collide_mask(self, self.fridge_boarder[2]):
            self.rect.y = 425
            self.rect.x = 847
            self.hp -= 1

        if pygame.sprite.collide_mask(self, self.fridge_boarder[3]):
            self.rect.y = 425
            self.rect.x = 847
            self.hp -= 1


        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            self.speedx = 3

            if not self.flag_skier_transform:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flag_skier_transform = True

        if keystate[pygame.K_LEFT]:
            self.speedx = -3

            if self.flag_skier_transform:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flag_skier_transform = False

        if keystate[pygame.K_DOWN]:
            self.speedy = 6

            if keystate[pygame.K_RIGHT]:
                self.speedx = 6

                if not self.flag_skier_transform:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flag_skier_transform = True

            if keystate[pygame.K_LEFT]:
                self.speedx = -6

                if self.flag_skier_transform:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flag_skier_transform = False

        self.rect.x += self.speedx
        self.rect.y += self.speedy


