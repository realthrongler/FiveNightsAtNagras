# Programmer(s):
# Date:
# Description:

import pygame
from pygame import *
from pygame.sprite import *

# define colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
### ADD ANY OTHER COLOUR CONSTANTS HERE ###

# define system constants
FPS = 60
WIDTH = 640
HEIGHT = 480
BGCOLOUR = BLACK ### CHANGE AS NEEDED ###

# initialize pygame, create window, start the clock
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

### ADD YOUR SPRITE CLASSES HERE ###

#class ImageSprite(Sprite):
#    def __init__(self, x, y, filename):                    # NEW sprite at (x,y)
#        Sprite.__init__(self)                              # init the Sprite object
#        self.image = image.load(filename).convert()        # loads the image from filename as the sprite  
#        self.rect = self.image.get_rect()                  # creates the rectangle around the sprite
#        self.rect.center = (x//2,y//2)                           

#    # semi-optional part
#    def update(self):
#        ### ADD MOVEMENT MODIFIERS HERE ###
#        self.rect.x += 5
#        self.rect.y -= 2
#        self.rect.center = (x//2,y//2)  
        

### ADD SPRITE INSTANCES HERE ###

#sprite = ImageSprite(x, y, "INSERT_IMAGE_FILENAME.jpg")

# group sprites
allSprites = pygame.sprite.Group()

# game loop
running = True
while running:
    # keep loop running at the right speed 
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        ### ADD ANY OTHER EVENTS HERE (KEYS, MOUSE, ETC.) ###
        
    # game loop updates (including movement)
    ### ADD ANY GAME LOOP UPDATES HERE ###
    
    # check for keypresses
    #keys = pygame.key.get_pressed()
    
    #if keys[K_LEFT]:
        # do something
    #if keys[K_RIGHT]:
        # do something 
    
    # game loop drawing
    ### ADD ANY GAME LOOP DRAWINGS HERE ###
    
    # background fill
    screen.fill(BGCOLOUR)
    
    # update position of sprites
    
    
    # render sprites on screen
    allSprites.draw(screen)
    
    # ***AFTER*** drawing everthing, flip (update) the display
    pygame.display.flip()
    
pygame.quit()
