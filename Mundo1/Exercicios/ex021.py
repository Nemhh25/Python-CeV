import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# Espera enquanto a música está tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)