import pygame
from skier import Skier
from obstacle import Tree
from Board import Border
from hp import Heart
from menu import Menu
from point_analys import PointAnalysis
from picture import Opisanie, Krest, Play_music, Stop_music
from music_playback import stop_music, play_music, play_music_wrong

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('snowboarder')
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    fps = 60
    running = True
    start_play = False
    flag_circle = False
    restart_play = False
    flag_doc = False
    flag_insert_point = False
    flag_music = True
    flag_music_menu = True
    flag_music_play = True
    flag_music_wrong = True
    flag_home = True
    point_skier = 0

    # создание груп со срайтами
    all_sprites = pygame.sprite.Group()
    Skier_sprite = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    heart_sprite = pygame.sprite.Group()
    Doc_sprite = pygame.sprite.Group()
    Krest_sprite = pygame.sprite.Group()
    Play_music_sprite = pygame.sprite.Group()
    Stop_music_sprite = pygame.sprite.Group()
    Elka_spite = pygame.sprite.Group()

    # создание границ экрана
    fridge_boarder = [Border(0, 1080, 1920, 1080, all_sprites, vertical_borders, horizontal_borders),
                      Border(0, 0, 1920, 0, all_sprites, vertical_borders, horizontal_borders),
                      Border(0, 0, 0, 1080, all_sprites, vertical_borders, horizontal_borders),
                      Border(1920, 0, 1920, 1080, all_sprites, vertical_borders, horizontal_borders),
                      Border(0, -300, 1920, -300, all_sprites, vertical_borders, horizontal_borders)]

    fridge_elka = list()

    # создание скаера
    Skier = Skier(Skier_sprite, fridge_boarder)
    Skier_sprite.add(Skier)

    heart_1 = Heart(heart_sprite, 1600, 0, Skier.hp)
    heart_2 = Heart(heart_sprite, 1760, 0, Skier.hp)

    Menu_Start = Menu(screen, (100, 200, 255), (730, 300, 400, 200), 'p l a y', (760, 300))
    Menu_Restart = Menu(screen, (100, 200, 255), (640, 500, 640, 200), 'r e s t a r t', (665, 500))
    Menu_point = Menu(screen, 'black', (640, 300, 640, 200), f'{Skier.point}', (900, 0))
    Menu_table_point = Menu(screen, (100, 200, 255), (0, 200, 10000, 200), f'', (10, 220))
    Menu_doc = Menu(screen, (100, 200, 255), (1000, 200, 10000, 200), f'', (1000, 220))
    Menu_exit = Menu(screen, (100, 200, 255), (730, 700, 400, 200), f'e x i t', (760, 710))
    Menu_go_home = Menu(screen, (100, 200, 255), (640, 800, 640, 200), f'g o h o m e', (647, 800))

    Point_analys = PointAnalysis()

    DOC = Opisanie()
    Doc_sprite.add(DOC)

    Krest_in_doc = Krest()
    Krest_sprite.add(Krest_in_doc)

    Play_m = Play_music()
    Play_music_sprite.add(Play_m)

    Stop_m = Stop_music()
    Stop_music_sprite.add(Stop_m)

    pygame.time.set_timer(pygame.USEREVENT, 1500)

    # игровой цикл
    while running:
        # описание
        if flag_doc and not start_play:
            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if 100 < pos[0] < 300 and 30 < pos[1] < 150 and flag_doc:
                        flag_doc = False

                if event.type == pygame.USEREVENT:
                    num = 0
                    if flag_circle:
                        flag_circle = False
                    else:
                        flag_circle = True
            Menu_doc.text_doc()

            Krest_sprite.draw(screen)
            pygame.display.flip()
            screen.fill((190, 230, 255))
        #  меню
        if not start_play and not flag_doc:
            if flag_music:
                if flag_music_menu:
                    play_music('music_menu.wav')
                    flag_music_menu = False
            num = 0
            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if 730 < pos[0] < 1130 and 300 < pos[1] < 500 and not restart_play:
                        Skier.hp = 2
                        start_play = True
                    if 640 < pos[0] < 1140 and 500 < pos[1] < 700 and restart_play:
                        Skier.hp = 2
                        flag_music_play = True
                        start_play = True
                    if 1000 < pos[0] < 1100 and 530 < pos[1] < 630:
                        flag_doc = True
                    if 730 < pos[0] < 1130 and 700 < pos[1] < 900 and not restart_play:
                        running = False
                    if 640 < pos[0] < 1280 and 800 < pos[1] < 1000 and restart_play:
                        restart_play = False
                        flag_music_menu = True
                        flag_music_play = True
                    if 750 < pos[0] < 850 and 530 < pos[1] < 630 and not restart_play:
                        if flag_music:
                            flag_music = False
                        else:
                            flag_music = True
                            flag_music_menu = True

            if restart_play:
                Menu_Restart.render()
                Menu_table_point.render()
                if flag_insert_point:
                    Point_analys.open()
                    Point_analys.recording_score(Skier.point)
                    Point_analys.close()
                    Point_analys.open()
                    max = Point_analys.max_score()
                    min = Point_analys.min_score()
                    avg = Point_analys.averages_score()
                    avg = str(avg)[0]
                    Point_analys.close()
                    flag_insert_point = False
                Menu_table_point.table_point(point_skier, avg, max, min)
                Menu_go_home.render()

                Skier.point = 0

            else:
                Menu_Start.render()
                Menu_exit.render()
                Doc_sprite.draw(screen)
                if flag_music:
                    Play_music_sprite.draw(screen)
                elif not flag_music:
                    stop_music()
                    Stop_music_sprite.draw(screen)

            pygame.display.flip()
            screen.fill((190, 230, 255))

        # начало игры
        if start_play and not flag_doc:
            if flag_home:
                heart_sprite.add(heart_1)
                heart_sprite.add(heart_2)
            if flag_music:
                if flag_music_play:
                    play_music('play.wav')
                    flag_music_play = False
            point_skier = 0
            if restart_play:
                heart_sprite.add(heart_1)
                heart_sprite.add(heart_2)

            running = Skier.flag_running
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.USEREVENT:
                    Skier.point += 1
                    Elka_spite.add(Tree())
                    # render(fridge_elka, Elka_spite)

            if Skier.hp == 0:
                heart_sprite.remove(heart_2)
                start_play = False
                restart_play = True
                flag_insert_point = True
                point_skier = Skier.point
                play_music_wrong('stop.wav')
            if Skier.hp == 1:
                heart_sprite.remove(heart_1)

            if pygame.sprite.spritecollide(Skier, Elka_spite, True):
                Skier.hp -= 1

            if pygame.sprite.spritecollide(fridge_boarder[4], Elka_spite, True):
                pass

            Skier_sprite.draw(screen)
            all_sprites.draw(screen)
            Skier_sprite.update()

            Elka_spite.draw(screen)
            Elka_spite.update()

            heart_sprite.draw(screen)
            Menu_point.point_print(f'{Skier.point}')
            pygame.display.flip()
            clock.tick(fps)
            screen.fill((190, 230, 255))
    pygame.quit()
