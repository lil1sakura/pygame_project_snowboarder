import pygame


class Menu:
    def __init__(self, screen, color, rext_cords, text, text_coords):
        self.screen = screen
        self.color = color
        self.rect_cords = rext_cords
        self.text = text
        self.text_cords = text_coords

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect_cords)
        myfont = pygame.font.SysFont('impact', 150)
        textsurface = myfont.render(self.text, False, (190, 230, 255))
        self.screen.blit(textsurface, self.text_cords)

    def point_print(self, text):
        myfont = pygame.font.SysFont('impact', 130)
        textsurface = myfont.render(text, False, 'black')
        self.screen.blit(textsurface, self.text_cords)

    def table_point(self, now, avg, max, min):
        myfont = pygame.font.SysFont('impact', 80)
        textsurface = myfont.render(f'N O W : {now} , A V G : {avg} , M A X : {max} , M I N : {min}',
                                    False, (190, 230, 255))
        self.screen.blit(textsurface, (10, 250))

    def text_doc(self):
        pygame.draw.rect(self.screen, (100, 200, 255), (300, 90, 1500, 780))
        myfont = pygame.font.SysFont('impact', 60).render('                                                  '
                                                          '   Snowborder', False, (190, 230, 255))
        self.screen.blit(myfont, (300, 90))
        myfont1 = pygame.font.SysFont('impact', 30).render(
            'Snowborder – это симулятор зимнего вида спорта по сноуборду.', False, (190, 230, 255))
        self.screen.blit(myfont1, (300, 160))
        myfont2 = pygame.font.SysFont('impact', 30).render(
            'Цель игры: спуститься с горы, преодолевая препятствия, при этом набрать наибольшее количество очков.',
            False, (190, 230, 255))
        self.screen.blit(myfont2, (300, 200))
        myfont3 = pygame.font.SysFont('impact', 30).render('Описание: ', False, (190, 230, 255))
        self.screen.blit(myfont3, (300, 240))
        myfont4 = pygame.font.SysFont('impact', 30).render('1) спуск с горы бесконечен;', False, (190, 230, 255))
        self.screen.blit(myfont4, (300, 270))
        myfont4 = pygame.font.SysFont('impact', 30).render('2) при спуске встречаются препятствия (ёлки), с которыми не нужно сталкиваться;', False, (190, 230, 255))
        self.screen.blit(myfont4, (300, 310))
        myfont5 = pygame.font.SysFont('impact', 30).render(
            '3) игрок управляет сноубордистом при помощи стрелок: сноубордист '
            'ускоряется при нажатии на стрелки: «вниз»,', False, (190, 230, 255))
        self.screen.blit(myfont5, (300, 350))
        myfont6 = pygame.font.SysFont('impact', 30).render(
            '«вправо» или «влево»;', False, (190, 230, 255))
        self.screen.blit(myfont6, (300, 390))
        myfont7 = pygame.font.SysFont('impact', 30).render(
            '4) сноубордист имеет «две жизни»: количество набранных'
            ' ранее очков уменьшается при столкновении с ёлками,', False, (190, 230, 255))
        self.screen.blit(myfont7, (300, 430))
        myfont8 = pygame.font.SysFont('impact', 30).render(
            'или когда он выходит за трассу;',
            False, (190, 230, 255))
        self.screen.blit(myfont8, (300, 470))
        myfont9 = pygame.font.SysFont('impact', 30).render(
            '5) игра имеет «счётчик», в котором сохраняется среднее, максимальное и минимальное количество очков,', False, (190, 230, 255))
        self.screen.blit(myfont9, (300, 510))
        myfont10 = pygame.font.SysFont('impact', 30).render(
            ' набранных игроком за время игр. ',
            False, (190, 230, 255))
        self.screen.blit(myfont10, (300, 550))
        myfont11 = pygame.font.SysFont('impact', 30).render(
            '                                                              '
            ' Попробуй и игра подарит тебе много эмоций и хорошее настроение!',
            False, (190, 230, 255))
        self.screen.blit(myfont11, (300, 700))
        myfont12 = pygame.font.SysFont('impact', 30).render(
            '                                                                                                         '
            '                     Желаем успеха!',
            False, (190, 230, 255))
        self.screen.blit(myfont12, (300, 750))



