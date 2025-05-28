#importing libraries
import pygame
from pygame import locals

pygame.init()

running = True
caption = ""

screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size, flags=pygame.RESIZABLE)

pygame.display.set_caption(caption)

while running:
    
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

pygame.quit()
