import pygame


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2, all_sprites, vertical_borders, horizontal_borders):
        super().__init__(all_sprites)
        self.all_sprites = all_sprites
        self.vertical_borders = vertical_borders
        self.horizontal_borders = horizontal_borders

        if x1 == x2:  # вертикальная стенка
            self.add(self.vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)

        else:  # горизонтальная стенка
            self.add(self.horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
