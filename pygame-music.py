import pygame
import os
pygame.init()
if os.path.exists('.mp3'):
    pygame.mixer.music.load('.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('Deu ruim')