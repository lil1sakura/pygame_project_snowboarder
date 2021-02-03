import pygame

pygame.init()


def play_music(file):
    pygame.mixer.music.load(f'song/{file}')
    pygame.mixer.music.play(loops=-1)


def play_music_wrong(file):
    pygame.mixer.music.load(f'song/{file}')
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()

